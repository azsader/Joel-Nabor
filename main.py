import disnake
from disnake.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
bot=commands.Bot(command_prefix=None, help_command=None)




if __name__=="__main__":
    try:
        bot.run(os.getenv("BOT_TOKEN"))
    except KeyboardInterrupt:
        pass