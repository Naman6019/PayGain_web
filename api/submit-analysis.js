import supabase from '../lib/supabaseClient.js';

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(204).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const { fullName, mobileNumber, emailAddress, city, interestedProduct, ...details } = req.body;

    if (!fullName || !mobileNumber || !city || !interestedProduct) {
      return res.status(400).json({ error: 'Required fields are missing.' });
    }

    const { data, error } = await supabase
      .from('analysis_requests')
      .insert([
        {
          full_name: fullName,
          mobile_number: mobileNumber,
          email_address: emailAddress || '',
          city: city,
          interested_product: interestedProduct,
          details: details
        }
      ]);

    if (error) {
      console.error('Supabase insert error:', error);
      return res.status(500).json({ error: 'Failed to submit analysis request.' });
    }

    return res.status(200).json({ success: true, message: 'Analysis request submitted successfully.' });
  } catch (err) {
    console.error('API error:', err);
    return res.status(500).json({ error: 'Internal server error.' });
  }
}
