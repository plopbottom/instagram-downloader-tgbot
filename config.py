import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
HIKERAPI_TOKEN = os.environ["HIKERAPI_TOKEN"]
ALLOWED_USER_IDS = {int(x) for x in os.environ.get("ALLOWED_USER_IDS", "").split(",") if x.strip()}
