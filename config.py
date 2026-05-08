import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX")
OWNER_ID = int(os.getenv("OWNER_ID"))

EMBED_COLOR = 0x5865F2
