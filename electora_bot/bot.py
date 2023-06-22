import importlib.metadata
import os
import platform

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
async def hello(ctx):
    description = (
        f"I'm {BOT.user.name} and I'm here to help you with your elections.\n"
        f"You can send me commands using the prefix '{_prefix}'.\n"
        f"I'm running at version {__version__} on Python {platform.python_version()}."
    )
    embed = discord.Embed(title="Hello", description=description)
    await ctx.send(embed=embed)
