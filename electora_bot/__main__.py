import os

import discord

from .bot import ElectoraBot

token = os.getenv("DISCORD_TOKEN")
guild_id = os.getenv("GUILD")
prefix = os.getenv("COMMAND_PREFIX")
intents = discord.Intents.default()

bot = ElectoraBot(prefix=prefix, intents=intents, guild_id=guild_id)
bot.run(token)
