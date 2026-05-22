import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")
DB_PATH = os.getenv("DB_PATH", "data.db")