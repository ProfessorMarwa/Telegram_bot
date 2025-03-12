import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "your_new_bot_token_here")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://your-new-bot-url.onrender.com/webhook")

if not BOT_TOKEN or not WEBHOOK_URL:
    raise ValueError("Missing BOT_TOKEN or WEBHOOK_URL. Ensure they are set in the .env file or Render environment variables.")
