import disnake
from disnake.ext import commands

class Ready(commands.cog):
    def __init__(self,bot: commands.Bot):
        self.bot=bot
    
    @commands.Cog.listener("ready")
    async def ready(self, bot):
        await self.bot.change_presence(status=disnake.Status.dnd, activity=disnake.Game("🛡️bot by ff.daethik"))
        print("ready")



def setup(bot): bot.add_cog(Ready(bot))