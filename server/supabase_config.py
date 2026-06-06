import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

url = os.environ.get("SB_URL")
key = os.environ.get("SB_PUBLISHABLE_KEY")

if not url or not key:
    raise ValueError("Supabase URL and key must be set in environment variables")

supabase = create_client(url, key)