import platform

import discord
from discord.ext import commands
from discord import app_commands


class GreeterCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="ping", description="Pong!")
    async def _ping(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("pong")

    @app_commands.command(
        name="hello", description="Hello. Allow me to introduce myself..."
    )
    async def _hello(self, interaction: discord.Interaction) -> None:
        description = (
            f"I'm {self.bot.user.name} and I'm here to help you with your elections.\n\n"  # noqa: E501
            f"I'm running at version {self.bot.version} on Python {platform.python_version()}."  # noqa: E501
        )
        embed = discord.Embed(title="Hello", description=description)
        await interaction.response.send_message(embed=embed)
