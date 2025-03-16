import logging
import os

from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.environ.get("NOTION_TOKEN")
DATABASE_ID = os.environ.get("DATABASE_ID")
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()

if not all([NOTION_TOKEN, DATABASE_ID]):
    raise ValueError("環境変数を設定してください")

logging.basicConfig(level=LOG_LEVEL)
