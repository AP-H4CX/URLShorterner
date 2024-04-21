# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()

# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "23007799"))
API_HASH = os.environ.get("API_HASH", "aa694ed52dbd072d6384053560132057")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6654040372:AAFKq29o0lChuii9cnRzTs7g9QsV63OlkaM")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS", "").split(",") if i.strip()] 
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Db Name")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://simonsi721:<W6rZYyotpXLYhuAF>@cluster0.ft0s6jb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "6036777486")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002084501753")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Moviesflix44") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start
LINK_BYPASS = "False"
