from disnake.ext import commands
import disnake
from main import config
class Embed(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot=bot

