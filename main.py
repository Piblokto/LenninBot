# Imports
import requests
import json
import discord
from discord.ext import commands
from discord.utils import get

# Define Bot Cal Prefix
bot = commands.Bot(command_prefix="!", description="Commie Bot", case_insensitive=True)

# Channel ID's

# Lennin Posting Channel ID
lennin_channel_id = 734601701666979942
# Stalin Hate Group Channel ID
stalin_channel_id = 734601735783317571
# Commie Girls Channel ID
commie_channel_id = 734601772450054196
# Aminal Channel ID
animal_channel_id = 737564889006211073

@bot.event
async def on_ready():
    # Printing Verification of Log in and Connection of Discord to terminal
    print(f"Logged in as {bot.user} and connected to Discord! (ID: {bot.user.id})")

    # Show "Playing Game"
    game = discord.Game(name= "with Ryan's sexuality")
    await bot.change_presence(activity = game)

    lennin_channel = bot.get_channel(lennin_channel_id)

# Responds with USSR Flag to !ussr or !communism
@bot.command(name = "ussr", aliases = ["communism"], help = "Responds with USSR Flag")
async def restart(ctx):
    await ctx.send("<:ussr:735408416280936448>")

# Responds with Embed when asked for source code with !sourcecode, !source, !code, or !open source
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

# Gives role to member who triggers !commie, !communist, or !commierole
@bot.command(name = "commie", aliases = ["communist", "commierole"], help = "Gives user commie role")
async def commie(ctx):
    role = ctx.guild.get_role(734601455792685087)
    await ctx.author.add_roles(role)
    await ctx.send(f"{ctx.author} now serves the motherland!")

# Sends random doggo photo UwU
@bot.command(name = "doggo", help = "Sends photo of a dog")
async def doggo(ctx):
    if ctx.channel.id == animal_channel_id:
        doggoresponse = requests.get("https://dog.ceo/api/breeds/image/random")
        dogpic = doggoresponse.json()
        await ctx.send(dogpic['message'])

# Sends random doggo fact UwU
@bot.command(name = "doggofact", help = "Sends fact of a dog")
async def doggofact(ctx):
    if ctx.channel.id == animal_channel_id:
        doggofactresponse = requests.get("https://some-random-api.ml/facts/dog")
        doggofact = doggofactresponse.json()
        dogfact = doggofact['fact']

        doggofact_embed = discord.Embed(
            title = f"Here's a random dog fact...",
            description = f"Did you know, {dogfact}",
            color = discord.Color.blue()
        )

        doggofact_embed.set_footer(
            text = "Doggo Fact",
            icon_url = "https://i.ibb.co/qxPpsT7/doggo.webp"
        )

        await ctx.send(embed = doggofact_embed)
        

# Sends random fox photo UwU
@bot.command(name = "fox", help = "Sends photo of a fox")
async def fox(ctx):
    if ctx.channel.id == animal_channel_id:
        foxresponse = requests.get("https://randomfox.ca/floof/")
        foxpic = foxresponse.json()
        await ctx.send(foxpic['image'])

# Sends random fox fact UwU
@bot.command(name = "foxfact", help = "Sends fact of a fox")
async def fox(ctx):
    if ctx.channel.id == animal_channel_id:
        foxfactresponse = requests.get("https://some-random-api.ml/facts/fox")
        foxfact = foxfactresponse.json()
        ffact = foxfact['fact']

        foxfact_embed = discord.Embed(
            title = f"Here's a random fox fact...",
            description = f"Did you know, {ffact}",
            color = discord.Color.blue()
        )

        foxfact_embed.set_footer(
            text = "Fox Fact",
            icon_url = "https://i.ibb.co/sFG4GsS/fox.jpg"
        )

        await ctx.send(embed = foxfact_embed)

# Scans message for instance of word and responds
# There are probably more organised ways to do this, however using the or command breaks it, same thing goes for putting separate @bot.event, on_message.
@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return
    # Responds with 5 different pog emotes to the mention of the word pog
    if 'pog' in message.content.split():
        await message.add_reaction("<:Pogey:729196572973465631>")
        await message.add_reaction("<:POGGERS:729196573178855494>")
        await message.add_reaction("<:PogU:729196572843311145>")
        await message.add_reaction("<:PogUU:729196571979284510>")
        await message.add_reaction("<:PeepoPog:729196572876996699>")
    elif 'Pog' in message.content.split():
        await message.add_reaction("<:Pogey:729196572973465631>")
        await message.add_reaction("<:POGGERS:729196573178855494>")
        await message.add_reaction("<:PogU:729196572843311145>")
        await message.add_reaction("<:PogUU:729196571979284510>")
        await message.add_reaction("<:PeepoPog:729196572876996699>")
    elif 'POG' in message.content.split():
        await message.add_reaction("<:Pogey:729196572973465631>")
        await message.add_reaction("<:POGGERS:729196573178855494>")
        await message.add_reaction("<:PogU:729196572843311145>")
        await message.add_reaction("<:PogUU:729196571979284510>")
        await message.add_reaction("<:PeepoPog:729196572876996699>")
    elif 'poggers' in message.content.split():
        await message.add_reaction("<:Pogey:729196572973465631>")
        await message.add_reaction("<:POGGERS:729196573178855494>")
        await message.add_reaction("<:PogU:729196572843311145>")
        await message.add_reaction("<:PogUU:729196571979284510>")
        await message.add_reaction("<:PeepoPog:729196572876996699>")
    elif 'Poggers' in message.content.split():
        await message.add_reaction("<:Pogey:729196572973465631>")
        await message.add_reaction("<:POGGERS:729196573178855494>")
        await message.add_reaction("<:PogU:729196572843311145>")
        await message.add_reaction("<:PogUU:729196571979284510>")
        await message.add_reaction("<:PeepoPog:729196572876996699>")  
    elif 'POGGERS' in message.content.split():
        await message.add_reaction("<:Pogey:729196572973465631>")
        await message.add_reaction("<:POGGERS:729196573178855494>")
        await message.add_reaction("<:PogU:729196572843311145>")
        await message.add_reaction("<:PogUU:729196571979284510>")
        await message.add_reaction("<:PeepoPog:729196572876996699>")  
    elif 'pogey' in message.content.split():
        await message.add_reaction("<:Pogey:729196572973465631>")
        await message.add_reaction("<:POGGERS:729196573178855494>")
        await message.add_reaction("<:PogU:729196572843311145>")
        await message.add_reaction("<:PogUU:729196571979284510>")
        await message.add_reaction("<:PeepoPog:729196572876996699>")
    elif 'Pogey' in message.content.split():
        await message.add_reaction("<:Pogey:729196572973465631>")
        await message.add_reaction("<:POGGERS:729196573178855494>")
        await message.add_reaction("<:PogU:729196572843311145>")
        await message.add_reaction("<:PogUU:729196571979284510>")
        await message.add_reaction("<:PeepoPog:729196572876996699>")
    elif 'POGEY' in message.content.split():
        await message.add_reaction("<:Pogey:729196572973465631>")
        await message.add_reaction("<:POGGERS:729196573178855494>")
        await message.add_reaction("<:PogU:729196572843311145>")
        await message.add_reaction("<:PogUU:729196571979284510>")
        await message.add_reaction("<:PeepoPog:729196572876996699>")
    elif 'pogchamp' in message.content.split():
        await message.add_reaction("<:Pogey:729196572973465631>")
        await message.add_reaction("<:POGGERS:729196573178855494>")
        await message.add_reaction("<:PogU:729196572843311145>")
        await message.add_reaction("<:PogUU:729196571979284510>")
        await message.add_reaction("<:PeepoPog:729196572876996699>")  
    elif 'Pogchamp' in message.content.split():
        await message.add_reaction("<:Pogey:729196572973465631>")
        await message.add_reaction("<:POGGERS:729196573178855494>")
        await message.add_reaction("<:PogU:729196572843311145>")
        await message.add_reaction("<:PogUU:729196571979284510>")
        await message.add_reaction("<:PeepoPog:729196572876996699>")
    elif 'PogChamp' in message.content.split():
        await message.add_reaction("<:Pogey:729196572973465631>")
        await message.add_reaction("<:POGGERS:729196573178855494>")
        await message.add_reaction("<:PogU:729196572843311145>")
        await message.add_reaction("<:PogUU:729196571979284510>")
        await message.add_reaction("<:PeepoPog:729196572876996699>")
    elif 'POGCHAMP' in message.content.split():
        await message.add_reaction("<:Pogey:729196572973465631>")
        await message.add_reaction("<:POGGERS:729196573178855494>")
        await message.add_reaction("<:PogU:729196572843311145>")
        await message.add_reaction("<:PogUU:729196571979284510>")
        await message.add_reaction("<:PeepoPog:729196572876996699>")

    # Anti Capitalism Commands, corrects people using "my", ect.    
    if 'my' in message.content.split():
        await message.channel.send(f"__**OUR**__")
    elif 'My' in message.content.split():
        await message.channel.send(f"__**OUR**__")
    elif 'MY' in message.content.split():
        await message.channel.send(f"__**OUR**__")
    elif 'mine' in message.content.split():
        await message.channel.send(f"__**OUR**__")
    elif 'Mine' in message.content.split():
        await message.channel.send(f"__**OUR**__")
    elif 'MINE' in message.content.split():
        await message.channel.send(f"__**OUR**__")
    elif 'private property' in message.content.split():
        await message.channel.send(f"Private property is a myth, shut up chud.")

    # Anti Stalin commands, becaue fuck stalin
    if 'stalin' in message.content.split():
        await message.channel.send(f"***Ewww STALIN***")
    elif 'Stalin' in message.content.split():
        await message.channel.send(f"***Ewww STALIN***")
    elif 'STALIN' in message.content.split():
        await message.channel.send(f"***Ewww STALIN***")

    # Communism Commands, congratulates people on usage of communist terms
    if 'our' in message.content.split():
        await message.add_reaction("<:ussr:735408416280936448>")
    elif 'us' in message.content.split():
        await message.add_reaction("<:ussr:735408416280936448>")
    elif 'we' in message.content.split():
        await message.add_reaction("<:ussr:735408416280936448>")

    await bot.process_commands(message) # this is needed because message.content is a greedy bitch

# Run bot, make sure to change the Token
bot.run("TOKEN", bot=True, reconnect=True)
