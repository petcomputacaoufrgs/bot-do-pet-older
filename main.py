import os
from decouple import config
from discord.ext import commands


# SETUP
bot_prefix = commands.Bot("pet.")
bot_prefix.remove_command("help")


# Loading the bot commands
def load_cogs(bot):
    # COMMANDS
    for file in os.listdir("commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f'commands.{cog}')

    # EVENTS
    for file in os.listdir("events"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f'events.{cog}')
    
    # HELP
    for file in os.listdir("help"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f'help.{cog}')
    
load_cogs(bot_prefix)


TOKEN = config("OFFICIAL_TOKEN")
bot_prefix.run(TOKEN)