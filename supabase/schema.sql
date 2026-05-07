-- Run this once in your Supabase SQL Editor before first deploy.
CREATE TABLE IF NOT EXISTS market_snapshot (
    id SERIAL PRIMARY KEY,
    fetched_at TIMESTAMPTZ DEFAULT now(),
    nifty50_value NUMERIC,
    nifty50_change NUMERIC,
    nifty50_pct_change NUMERIC,
    niftybank_value NUMERIC,
    niftybank_change NUMERIC,
    niftybank_pct_change NUMERIC,
    fii_buy NUMERIC,
    fii_sell NUMERIC,
    fii_net NUMERIC,
    fii_date TEXT,
    dii_buy NUMERIC,
    dii_sell NUMERIC,
    dii_net NUMERIC,
    fd_rates JSONB,
    nifty_trend JSONB,
    announcements JSONB
);

CREATE TABLE IF NOT EXISTS analysis_requests (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMPTZ DEFAULT now(),
    full_name TEXT NOT NULL,
    mobile_number TEXT NOT NULL,
    email_address TEXT NOT NULL,
    city TEXT NOT NULL,
    interested_product TEXT NOT NULL
);
