import supabase from '../lib/supabaseClient.js';

async function sendSubmissionEmailWebhook(payload) {
  const webhookUrl = process.env.FORM_ALERT_WEBHOOK_URL;
  if (!webhookUrl) return;

  const { fullName, mobileNumber, whatsappNumber, emailAddress, city, occupation, interestedProduct, message } = payload;

  const body = {
    event: 'new_form_submission',
    subject: `New PayGain form submission: ${fullName}`,
    text: [
      `Name: ${fullName}`,
      `Mobile: ${mobileNumber}`,
      `WhatsApp: ${whatsappNumber || '-'}`,
      `Email: ${emailAddress || '-'}`,
      `City: ${city}`,
      `Occupation: ${occupation || '-'}`,
      `Interested Product: ${interestedProduct}`,
      `Message: ${message || '-'}`
    ].join('\n'),
    data: payload
  };

  try {
    const response = await fetch(webhookUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body)
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.error('Email webhook responded with non-2xx:', response.status, errorText);
    }
  } catch (notifyErr) {
    // Notification failure should not break form submission.
    console.error('Email webhook notify failed:', notifyErr);
  }
}

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
    const {
      fullName,
      age,
      mobileNumber,
      whatsappNumber,
      emailAddress,
      city,
      occupation,
      message,
      interestedProduct,
      ...details
    } = req.body;

    if (!fullName || !mobileNumber || !city || !interestedProduct) {
      return res.status(400).json({ error: 'Required fields are missing.' });
    }

    const parsedAge = age ? Number.parseInt(age, 10) : null;
    const gender = details.life_gender || details.gender || '';

    const { data, error } = await supabase
      .from('analysis_requests')
      .insert([
        {
          full_name: fullName,
          age: Number.isNaN(parsedAge) ? null : parsedAge,
          mobile_number: mobileNumber,
          whatsapp_number: whatsappNumber || '',
          email_address: emailAddress || '',
          city: city,
          occupation: occupation || '',
          gender: gender,
          message: message || '',
          interested_product: interestedProduct,
          details: details
        }
      ]);

    if (error) {
      console.error('Supabase insert error:', error);
      return res.status(500).json({ error: 'Failed to submit analysis request.' });
    }

    await sendSubmissionEmailWebhook({
      fullName,
      age: Number.isNaN(parsedAge) ? null : parsedAge,
      mobileNumber,
      whatsappNumber: whatsappNumber || '',
      emailAddress: emailAddress || '',
      city,
      occupation: occupation || '',
      gender,
      message: message || '',
      interestedProduct,
      details
    });

    return res.status(200).json({ success: true, message: 'Analysis request submitted successfully.' });
  } catch (err) {
    console.error('API error:', err);
    return res.status(500).json({ error: 'Internal server error.' });
  }
}
