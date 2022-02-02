import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://semoo:semoo@semo.acu5d.mongodb.net/semo?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "ahmedelnqyb")
ALIVE_NAME = getenv("ALIVE_NAME", "𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "barelnqyb")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "elnqyb")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1645561253").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/UUCCTT/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
