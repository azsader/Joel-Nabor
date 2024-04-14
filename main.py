import disnake
from disnake.ext import commands
import os
from dotenv import load_dotenv
import json
with open("config.json") as f:
    config=json.load(f)
load_dotenv()
bot=commands.Bot(command_prefix=None, help_command=None)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


if __name__=="__main__":
    try:
        bot.run(os.getenv("BOT_TOKEN"))
    except KeyboardInterrupt:
        pass