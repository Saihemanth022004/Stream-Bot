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
    API_ID = int(getenv('API_ID', '16681004'))
    API_HASH = str(getenv('API_HASH', '161b61f5a06dd299a3d88a3384b9f104'))
    BOT_TOKEN = str(getenv('BOT_TOKEN' , '6881178610:AAECZjGP6SETmxlz4xblU2F8S4CbQGDKH3A'))
    name = str(getenv('name', 'File_to_Link_2024_Bot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002022120998'))
    NEW_USER_LOG = int(getenv('NEW_USER_LOG', '-1002022120998'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "6646028262").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'Sorry_Sorry_Galti_Ho_Gai'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME')) #dont need to fill anything here
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',True))
    if HAS_SSL:
        URL = "".format(FQDN)
    else:
        URL = "".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://deendayaldeenu84:r2sXoWGr3oYESdmS@cluster0.yhrcfhi.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'Deendayal_dhakad')) 
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split()))   
    BAN_CHNL = list(set(int(x) for x in str(getenv("BAN_CHNL", "")).split()))   
    
