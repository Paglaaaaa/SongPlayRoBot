import os
API_ID = 7103848
API_HASH = b9d7fd9a74488892695ffede4d597417
BOT_TOKEN = 1766427674:AAHcSlfW-YezQqWwm2zdU3Cgk5LtHOpEJJ4
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "").split()})
