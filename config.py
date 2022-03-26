import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5103483960:AAHSWYnhSZVgXURrvjs8xhdIaXOgT-Gx31U")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "14130870"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a17d645e8c768c544773699ee2ee7fb0")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001676442171"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "2056631488"))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001720280140"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Halo {first}\n\nSaya dapat menyimpan file pribadi di Saluran Tertentu dan pengguna lain dapat mengaksesnya dari tautan khusus.\nJika bot mengalami kendala harap lapor ke @HilmySakti Ya!")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1537048235").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Halo {first}\n\n<b>Anda harus bergabung di Channel/Grup saya untuk menggunakan saya\n\nSilakan bergabung dengan Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'False':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "sgc.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)