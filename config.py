import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
REPORT_CHAT_ID = int(os.getenv("REPORT_CHAT_ID"))
TECH_CHAT_ID = int(os.getenv("TECH_CHAT_ID", REPORT_CHAT_ID))

API_BASE_URL = os.getenv("API_BASE_URL", "").rstrip("/")
API_REPORT_DAILY = os.getenv("API_REPORT_DAILY", "/api/reports/daily/")
API_REPORT_RANGE = os.getenv("API_REPORT_RANGE", "/api/reports/range/")
API_HEALTH = os.getenv("API_HEALTH", "/api/reports/health/")
API_BOT_TOKEN = os.getenv("API_BOT_TOKEN")
API_USERNAME = os.getenv("API_USERNAME", "1")
API_PASSWORD = os.getenv("API_PASSWORD", "1")

TZ = os.getenv("TZ", "Asia/Tashkent")
HTTP_TIMEOUT = float(os.getenv("HTTP_TIMEOUT", 20))
HTTP_RETRIES = int(os.getenv("HTTP_RETRIES", 2))

assert BOT_TOKEN, "BOT_TOKEN is required"
assert API_BASE_URL, "API_BASE_URL is required"
