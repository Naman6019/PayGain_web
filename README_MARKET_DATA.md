# PayGain Market Data Infrastructure

This project contains a serverless backend for fetching NSE market data and syncing it with Supabase.

## Deployment Instructions

1. **Database Setup**
   - Create a Supabase project.
   - Run the SQL script found in `supabase/schema.sql` in the Supabase SQL Editor.

2. **Environment Variables**
   - Add all 4 env variables in Vercel Dashboard -> Project Settings -> Environment Variables.
     - `SUPABASE_URL`
     - `SUPABASE_SERVICE_KEY`
     - `SUPABASE_ANON_KEY`
     - `CRON_SECRET`
   - Run `vercel env pull .env.local` to sync locally.

3. **Configure CRON Secret**
   - Replace `REPLACE_WITH_CRON_SECRET` in both cron entries in `vercel.json` with your actual `CRON_SECRET`.

4. **Frontend Configuration**
   - Update the two `<meta>` tags in `pulse.html` with your actual Supabase URL and anon key:
     ```html
     <meta name="supabase-url" content="YOUR_SUPABASE_URL">
     <meta name="supabase-anon-key" content="YOUR_ANON_KEY">
     ```

5. **Manual Testing**
   - You can trigger a fetch manually by curling your deployment URL (or localhost):
     `curl "https://website-pg-two.vercel.app/api/fetch-market-data?secret=YOUR_SECRET"`

6. **Cron Schedule**
   - Market Open: 9:00 AM IST (3:30 UTC), Mon-Fri
   - Market Close: 3:30 PM IST (10:00 UTC), Mon-Fri

7. **Updating FD Rates**
   - The Fixed Deposit rates are hardcoded. You can update them in `/lib/fetchNSE.js` directly whenever Banks update their interest rates.

8. **Important Note**
   - The NSE APIs only return live data during Indian market hours.
