# PayGain Website Deployment Prompt for ChatGPT

You can copy and paste the text below into ChatGPT to get precise, step-by-step instructions on how to migrate your site to cPanel.

***

**Copy everything below this line:**
___

I need step-by-step instructions on how to deploy my company's website to a standard cPanel hosting environment. 

Here is a summary of my website's architecture and files:

### 1. Frontend Architecture (Static Files)
- **HTML Files:** `index.html`, `about_us.html`, `faq.html`, `career.html`, `contact.html`, `analysis_form.html`, `pulse.html`.
- **Assets:** An `assets/` folder containing images, logos, and PDF documents.
- **Styling:** Tailwind CSS (loaded via CDN) and FontAwesome.
- **Frontend Logic:** Vanilla JavaScript embedded within the HTML files.
- **Database Connection:** Supabase (used for tracking market data and form submissions).

### 2. Backend Architecture (Node.js / Vercel Serverless)
My project is currently set up as a Vercel project (`type: module` in `package.json`).
- **`api/` Folder:** Contains Vercel Serverless Functions written in Node.js. These handle form submissions (`/api/submit-analysis`).
- **`lib/` Folder:** Contains shared Node.js utility scripts.
- **Dependencies:** `@supabase/supabase-js`, `@vercel/functions`.

### My Goal & Constraints:
I need to move this entirely to my company's domain hosted on **cPanel**. 
Since cPanel is traditionally built for PHP and static files, I need to know the best way to handle my Node.js serverless functions. 

Please provide step-by-step instructions that cover:
1. How to upload and map the static HTML/CSS/JS frontend files using the cPanel File Manager (into `public_html`).
2. The best approach for handling my Node.js `api/` backend on cPanel. (Should I use cPanel's "Setup Node.js App" feature? Should I keep the APIs hosted on Vercel and just point my static frontend to the Vercel URL? Or should I rewrite the APIs to PHP?)
3. How to manage environment variables (like my Supabase secret keys) securely in cPanel if I host the Node app there.
4. How to ensure routing works correctly (e.g., ensuring form submissions mapped to `/api/submit-analysis` still function properly).

Please give me a clear, prioritized recommendation on the easiest and most reliable path forward.
