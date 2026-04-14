const NSE_HEADERS = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
  'Referer': 'https://www.nseindia.com',
  'Accept': 'application/json'
};

export const FD_RATES = {
  SBI:   { '1yr': 6.80, '2yr': 7.00, '3yr': 6.75, '5yr': 6.50 },
  HDFC:  { '1yr': 6.60, '2yr': 7.25, '3yr': 7.00, '5yr': 7.00 },
  ICICI: { '1yr': 6.70, '2yr': 7.25, '3yr': 7.00, '5yr': 7.00 }
};

async function getNSESession() {
  const headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
  };
  const res1 = await fetch('https://www.nseindia.com', { headers });
  const cookies1 = res1.headers.get('set-cookie') || '';
  await new Promise(r => setTimeout(r, 1000));
  const res2 = await fetch('https://www.nseindia.com/market-data/live-equity-market', {
    headers: { ...headers, 'Cookie': cookies1 }
  });
  const cookies2 = res2.headers.get('set-cookie') || '';
  const finalCookie = [cookies1, cookies2]
    .join('; ')
    .split(';')
    .map(c => c.trim())
    .filter(c => c.includes('='))
    .map(c => c.split('=').slice(0,2).join('='))
    .join('; ');
  return finalCookie;
}

export default async function fetchAllMarketData() {
  const data = {
    nifty50: null,
    niftyBank: null,
    fii: null,
    dii: null,
    niftyTrend: null,
    announcements: null,
    fdRates: FD_RATES
  };

  const cookieString = await getNSESession();
  console.log('NSE Cookie:', cookieString);
  const fetchHeaders = { ...NSE_HEADERS };
  if (cookieString) {
    fetchHeaders['Cookie'] = cookieString;
  }

  // 1. NSE All Indices
  try {
    const indicesRes = await fetch('https://www.nseindia.com/api/allIndices', { headers: fetchHeaders });
    console.log('NSE Indices raw response status:', indicesRes.status);
    
    const textBody = await indicesRes.text();
    console.log('NSE Indices raw body:', textBody);

    if (indicesRes.ok) {
      const json = JSON.parse(textBody);
      const nifty50 = json.data.find(idx => idx.indexSymbol === "NIFTY 50");
      const niftyBank = json.data.find(idx => idx.indexSymbol === "NIFTY BANK");
      
      if (nifty50) {
        data.nifty50 = {
          value: nifty50.last,
          change: nifty50.change,
          percentChange: nifty50.percentChange
        };
      }
      if (niftyBank) {
        data.niftyBank = {
          value: niftyBank.last,
          change: niftyBank.change,
          percentChange: niftyBank.percentChange
        };
      }
    }
  } catch (err) {
    console.error('Failed to fetch NSE indices:', err);
  }

  // 2. FII / DII Data
  try {
    const res = await fetch('https://www.nseindia.com/api/fiidiiTradeReact', { headers: fetchHeaders });
    if (res.ok) {
      const json = await res.json();
      if (Array.isArray(json) && json.length > 0) {
        const fiiObj = json.find(item => item.category && item.category.includes('FII'));
        const diiObj = json.find(item => item.category === 'DII');
        
        if (fiiObj) {
          data.fii = {
            buyValue: fiiObj.buyValue,
            sellValue: fiiObj.sellValue,
            netValue: fiiObj.netValue,
            date: fiiObj.date
          };
        }
        if (diiObj) {
          data.dii = {
            buyValue: diiObj.buyValue,
            sellValue: diiObj.sellValue,
            netValue: diiObj.netValue
          };
        }
      }
    }
  } catch (err) {
    console.error('Failed to fetch FII/DII data:', err);
  }

  // 3. Nifty Trend (30d, 6mo, 1y, 5y)
  try {
    const ranges = ['30d', '6mo', '1y', '5y'];
    const trendData = {};
    
    await Promise.all(ranges.map(async (rng) => {
      const interval = rng === '5y' ? '1wk' : '1d';
      const res = await fetch(`https://query1.finance.yahoo.com/v8/finance/chart/%5ENSEI?interval=${interval}&range=${rng}`);
      if (res.ok) {
        const json = await res.json();
        const result = json.chart.result[0];
        const timestamps = result.timestamp;
        const closes = result.indicators.quote[0].close;
        
        if (timestamps && closes) {
          trendData[rng] = timestamps.map((ts, i) => {
            const dateStr = new Date(ts * 1000).toISOString().split('T')[0];
            return { date: dateStr, close: closes[i] };
          }).filter(item => item.close !== null);
        }
      }
    }));
    
    data.niftyTrend = Object.keys(trendData).length > 0 ? trendData : null;
  } catch (err) {
    console.error('Failed to fetch Nifty trend:', err);
  }

  // 4. NSE Announcements
  try {
    const res = await fetch('https://www.nseindia.com/api/corporate-announcements?index=equities', { headers: fetchHeaders });
    if (res.ok) {
      const json = await res.json();
      const annData = Array.isArray(json) ? json : (json.data || []);
      if (annData.length > 0) {
        data.announcements = annData.slice(0, 10).map(item => {
          return {
            headline: item.desc || item.subject || '',
            company: item.sm_name || item.company || '',
            timestamp: item.an_dt || item.bcastDttm || '',
            description: item.attchmntText ? (item.attchmntText.length > 800 ? item.attchmntText.substring(0, 800) + '...' : item.attchmntText) : ''
          };
        });
      }
    }
  } catch (err) {
    console.error('Failed to fetch NSE announcements:', err);
  }

  return data;
}
