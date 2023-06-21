import os

import discord
from discord.ext import commands

_prefix = os.getenv("COMMAND_PREFIX")
_intents = discord.Intents.default()
_intents.message_content = True
BOT = commands.Bot(command_prefix=_prefix, intents=_intents)


@BOT.command()
async def ping(ctx):
    await ctx.send("pong")
