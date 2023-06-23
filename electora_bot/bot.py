import importlib.metadata

import discord
from discord.ext import commands

from .cogs.admin import AdminCog
from .cogs.ballot import BallotCog
from .cogs.greeter import GreeterCog

COGS = (AdminCog, BallotCog, GreeterCog)


class ElectoraBot(commands.Bot):
    def __init__(
        self, prefix: str, intents: discord.Intents, guild_id: int = None
    ) -> None:
        super().__init__(command_prefix=prefix, intents=intents)
        self.version = importlib.metadata.version("electora_bot")
        self.guild = discord.Object(id=guild_id) if guild_id else None

    async def sync(self):
        if self.guild:
            self.tree.copy_global_to(self.guild)
        await self.tree.sync()

    async def setup_hook(self) -> None:
        for cog in COGS:
            await self.add_cog(cog(self))
        await self.sync()
