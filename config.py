import os

API_ID = API_ID = 24262622

API_HASH = os.environ.get("API_HASH", "50831eb3329ed9c0557aa2bc6aa34376")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6537482060:AAFMrvWgLcHOhOgzR1kTBZjAucRPVXz63K4")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1477222048))

LOG = -4037966589

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1477222048").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


