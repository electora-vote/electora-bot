import discord
from discord import app_commands
from discord.ext import commands


class AdminCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="sync", description="Syncs the bot's slash commands")
    @app_commands.checks.has_permissions(administrator=True)
    async def _sync(self, interaction: discord.Interaction) -> None:
        self.bot.sync()
        await interaction.response.send_message("Synced slash commands")
