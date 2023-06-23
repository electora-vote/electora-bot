import discord
from discord import app_commands
from discord.ext import commands

APP_URL = "https://app.electora.eu"


class CreateBallot(discord.ui.View):
    def __init__(self) -> None:
        super().__init__()
        button = discord.ui.Button(
            label="Create Ballot",
            style=discord.ButtonStyle.primary,
            url=f"{APP_URL}/#ballot/create",
        )
        self.add_item(button)


class BallotCog(commands.GroupCog, name="ballot"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__()

    @app_commands.command(name="create", description="Create a new ballot")
    async def _create(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(view=CreateBallot())
