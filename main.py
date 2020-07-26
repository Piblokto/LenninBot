# Imports
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

# Scans message for instance of word and responds
# I would 
@bot.event
async def on_message(message):
    # Responds with 5 different pog emotes to the mention of the word pog
    if 'pog' in message.content:
        await message.add_reaction("<:Pogey:729196572973465631>")
        await message.add_reaction("<:POGGERS:729196573178855494>")
        await message.add_reaction("<:PogU:729196572843311145>")
        await message.add_reaction("<:PogUU:729196571979284510>")
        await message.add_reaction("<:PeepoPog:729196572876996699>")

    # Anti Capitalism Commands, corrects people using "my", ect.    
    if 'my' in message.content:
        await message.channel.send(f"__**OUR**__")
    elif 'mine' in message.content:
        await message.channel.send(f"__**OUR**__")
    elif 'private property' in message.content:
        await message.channel.send(f"Private property is a myth, shut up chud.")
    
    # Communism Commands, congratulates people on usage of communist terms
    if 'our' in message.content:
        await message.add_reaction("<:ussr:735408416280936448>")
    elif 'us' in message.content:
        await message.add_reaction("<:ussr:735408416280936448>")
    elif 'we' in message.content:
        await message.add_reaction("<:ussr:735408416280936448>")
 
    
    await bot.process_commands(message) # this is needed because message.content is a greedy bitch

# Run bot, make sure to change the Token
bot.run("TOKEN", bot=True, reconnect=True)