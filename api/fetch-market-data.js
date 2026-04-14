import { waitUntil } from '@vercel/functions';
import fetchAllMarketData from '../lib/fetchNSE.js';
import supabase from '../lib/supabaseClient.js';

export const maxDuration = 30;

export default async function handler(req, res) {
  const authHeader = req.headers.authorization;
  const paramSecret = new URL(req.url, 'https://base').searchParams.get('secret');

  if (
    authHeader !== `Bearer ${process.env.CRON_SECRET}` &&
    paramSecret !== process.env.CRON_SECRET
  ) {
    return res.status(401).json({ error: 'Unauthorized' });
  }

  res.status(202).json({ status: 'accepted', message: 'Fetch in progress' });

  waitUntil((async () => {
    try {
      const data = await fetchAllMarketData();
      const { error } = await supabase.from('market_snapshot').insert([{
        nifty50_value:        data.nifty50?.value,
        nifty50_change:       data.nifty50?.change,
        nifty50_pct_change:   data.nifty50?.percentChange,
        niftybank_value:      data.niftyBank?.value,
        niftybank_change:     data.niftyBank?.change,
        niftybank_pct_change: data.niftyBank?.percentChange,
        fii_buy:              data.fii?.buyValue,
        fii_sell:             data.fii?.sellValue,
        fii_net:              data.fii?.netValue,
        fii_date:             data.fii?.date,
        dii_buy:              data.dii?.buyValue,
        dii_sell:             data.dii?.sellValue,
        dii_net:              data.dii?.netValue,
        fd_rates:             data.fdRates,
        nifty_trend:          data.niftyTrend,
        announcements:        data.announcements
      }]);
      if (error) console.error('Supabase insert error:', error);
    } catch (err) {
      console.error('Market fetch error:', err);
    }
  })());
}
