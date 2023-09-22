import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "1BVtsOKIBuwJIMK-prg3QrtJSB1J6zt5PVzrc7GiWyiYHY_eIf93aN0dVfyfb7ta8YHi_on4oowUy8j9eB7-Gctaz9qZdoBfQ5PLkRaurXRb24-e62it1lrctMUlZ9KNjXyKnV4rD8yMYVtBklkhLY-jjQf2VNySgrS2Mhnlyhb49z-OzJMBuI3YxC23VaWxLFBPm65RH9oXl21e2Ea12wgJ6woDYXsXT6N82hnA2EYbVj3CJJSF1WJmGaZAmmXHIhw_-fcZk-vsXEdhBCYJuEz1z4m_LXzE1oWG425HrExwPsiGQykM0y7OCMPdUmB3aAtzApevgWCvkrJ4rth2ZwPp7MBPgt-0=")
BOT_TOKEN = getenv("BOT_TOKEN" ,"6431081969:AAHrnUc1me1SffMgcyvI9THYclgTiRgFE8A")
BOT_NAME = getenv("BOT_NAME" ,"Nnnnn")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "LaylaBots")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/9b13ea3ce046a1a5c8098.png")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME" ,"Princess_music_robot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Dead0XD")
OWNER_NAME = getenv("OWNER_NAME", "HEROGAMERS1")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "AwesomeSupport")
PROJECT_NAME = getenv("PROJECT_NAME", "VCPlayBot2.0")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/QueenArzoo/VCPlayBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5096741943").split()))
