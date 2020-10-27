# Imports
import configparser
import os

import discord
from discord.ext import commands
from discord.utils import get

# Define Config
config = configparser.ConfigParser()

# Find correct path for config file
if (os.path.exists('config.ini')):
    config.read('config.ini')
else:
    config.read(os.path.dirname(__file__) + os.path.sep + 'config.ini')

prefix = config.get("Bot_Data", "Bot_Prefix")
bot = commands.Bot(command_prefix=prefix, description="Bot")

# On Startup
@bot.event
async def on_ready():
    # Log Bot Status on Startup
    print(f"Logged in as {bot.user} and connected to Discord! (ID: {bot.user.id})")

    # Show Status
    game = discord.Game(name= "Playing with Ryan\'s sexuality")
    await bot.change_presence(activity = game)

@bot.command(name = "sourcecode", aliases = ["source", "code", "opensource"], help = "Responds with source code of bot")
async def source(ctx):
    
    sourcecode_embed = discord.Embed(
        title = f"{bot.user.name} is fully Open Source!",
        description = f"Feel free to view the source code here https://github.com/Piblokto/LenninBot under our MIT licence.",
        color = discord.Color.red()
    )
    sourcecode_embed.set_footer(
        text = "Lennin Bot",
        icon_url = "https://i.ibb.co/4sYK2CH/profilepic.png"
    )

    await ctx.send(embed = sourcecode_embed)

@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return
    
    parsedmsg = message.content.lower().split()

    if 'pog' in parsedmsg:
        await message.add_reaction("<:Pogey:729196572973465631>")
        await message.add_reaction("<:POGGERS:729196573178855494>")
        await message.add_reaction("<:PogU:729196572843311145>")
        await message.add_reaction("<:PogUU:729196571979284510>")
        await message.add_reaction("<:PeepoPog:729196572876996699>")

    if 'our' in parsedmsg:
        await message.add_reaction("<:USSR:770527295529287690>")
    
    if 'my' in parsedmsg:
        await message.channel.send(f"__**OUR**__")
    
    await bot.process_commands(message)

token = config.get("Bot_Data", "Bot_Token")
bot.run(token, bot=True, reconnect=True)
