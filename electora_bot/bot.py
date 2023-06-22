import importlib.metadata
import os

import discord
from discord.ext import commands

__version__ = importlib.metadata.version("electora_bot")
_prefix = os.getenv("COMMAND_PREFIX")
_intents = discord.Intents.default()
_intents.message_content = True
BOT = commands.Bot(command_prefix=_prefix, intents=_intents)


@BOT.command()
async def ping(ctx):
    await ctx.send("pong")


@BOT.command()
async def version(ctx):
    await ctx.send(f"I'm Electora Bot version {__version__}")
