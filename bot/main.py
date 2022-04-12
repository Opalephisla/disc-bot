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


messagecounts = {}

@bot.command()
async def serverstats(ctx):
    embed=discord.Embed(title=f"Statystyki serwera {ctx.guild.name}")
    embed.add_field(name="Users:", value=ctx.guild.member_count, inline=False)
    embed.add_field(name="Channels:", value=len(ctx.guild.channels), inline=False)
    embed.add_field(name="Messages sent:", value=messagecounts[ctx.guild.id], inline=False)
    await ctx.send(embed=embed)

#on_message event handler for users ending sentences with "quoi" and replying "feur"
@bot.event
async def on_message(message):

    # counts how many messages the user sent in his lifetime and replies with an embed of his stats
    if message.author.id == bot.user.id:
        return

    if message.guild.id not in messagecounts.keys():
        messagecounts[message.guild.id] = 0
    messagecounts[message.guild.id] += 1

    if message.content.endswith("quoi"):
        await message.channel.send("feur")
        
server.server()
bot.run(TOKEN)
