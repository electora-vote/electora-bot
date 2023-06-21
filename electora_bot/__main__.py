import os

from .bot import BOT

TOKEN = os.getenv("DISCORD_TOKEN")
BOT.run(TOKEN)
