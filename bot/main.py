import discord
import os
#import pynacl
#import dnspython
import server
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")
    # change bot status to "Studying WEB Development"
    await bot.change_presence(activity=discord.Game(name="Studying WEB Development"))

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

#on_message event handler for users ending sentences with "quoi" and replying "feur"
@bot.event
async def on_message(message):
    if message.content.endswith("quoi"):
        await message.channel.send("feur")

    # counts how many messages are sent consecutively by a user
    if message.author.id == bot.user.id:
        return
    if message.author.id not in server.users:
        server.users[message.author.id] = [message.author, 1]
    else:
        server.users[message.author.id][1] += 1
    
    # if user has sent more than 5 messages consecutively, delete them
    if server.users[message.author.id][1] > 5:
        message.author.delete()
        await message.channel.send(f"{message.author.mention} has been deleted for spamming")
        
server.server()
bot.run(TOKEN)
