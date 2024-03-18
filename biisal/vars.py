# (c) adarsh-goel (c) @biisal
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()
bot_name = "File to Link Bot"
bisal_channel = "https://telegram.me/Deendayal_dhakad"
bisal_grp = "https://t.me/BollyWood_Hollywood_South_Movie7"

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '20738979'))
    API_HASH = str(getenv('API_HASH', 'a6d015153068a35390a336fe0a38dd64'))
    BOT_TOKEN = str(getenv('BOT_TOKEN' , '6683650338:AAEkBqC01ihqCSwpqO_8ZvHsB7QEGzB6fig'))
    name = str(getenv('name', 'Drnboss_bot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '3'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001586622410'))
    NEW_USER_LOG = int(getenv('NEW_USER_LOG', '-1001586622410'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5658395021").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'venom_darshu'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME')) #dont need to fill anything here
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',True))
    if HAS_SSL:
        URL = "https://stream-bot-t7d8.onrender.com/".format(FQDN)
    else:
        URL = "https://stream-bot-t7d8.onrender.com/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://venomdarshu0:darshu567@cluster0.mwgkkci.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', "-100158662241")
    vdmoviez')) 
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split()))   
    BAN_CHNL = list(set(int(x) for x in str(getenv("BAN_CHNL", "")).split()))   
    
