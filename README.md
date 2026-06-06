# Retail Radar

AI-powered retail trend forecasting using TikTok social signals and machine learning.

## Project Structure

    retail_radar/
    ├── client/          # Next.js frontend
    │   ├── app/
    │   │   └── page.tsx
    │   └── components/
    ├── server/          # Python scraper + ML model
    │   ├── supabase_config.py        # Supabase connection
    │   ├── scraper.py   # TikTok scraper
    ├── .gitignore
    └── README.md

## Tech Stack

- **Frontend** — Next.js (App Router) + Tailwind CSS
- **Backend** — Python
- **Scraping** — TikTokApi + Playwright (browser automation)
- **Database** — Supabase
- **ML** — Coming soon