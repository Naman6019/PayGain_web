import supabase from '../lib/supabaseClient.js';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const { fullName, mobileNumber, emailAddress, city, interestedProduct } = req.body;

    if (!fullName || !mobileNumber || !emailAddress || !city || !interestedProduct) {
      return res.status(400).json({ error: 'All fields are required.' });
    }

    const { data, error } = await supabase
      .from('analysis_requests')
      .insert([
        {
          full_name: fullName,
          mobile_number: mobileNumber,
          email_address: emailAddress,
          city: city,
          interested_product: interestedProduct
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
