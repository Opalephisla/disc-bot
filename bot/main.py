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
        
server.server()
bot.run(TOKEN)
