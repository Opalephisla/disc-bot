import discord
import os
#import pynacl
#import dnspython
import server
import interactions
from discord.ext import commands
from discord_slash import SlashCommand

bot = commands.Bot(command_prefix="!")

client = interactions.Client(token="...")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello from discord.py!")

@client.command(
    name="test",
    description="this is just a testing command."
)
async def test(ctx):
    await ctx.send("Hello from discord-interactions!")

@slash.slash(name="ping", guild_ids=guild_ids)
async def _ping(ctx):
    await ctx.send("Pong!")


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
    embed=discord.Embed(title=f"Statistiques du serveur {ctx.guild.name}")
    embed.add_field(name="Nombre d'utilisateurs:", value=ctx.guild.member_count, inline=False)
    embed.add_field(name="Nombres de salons:", value=len(ctx.guild.channels), inline=False)
    embed.add_field(name="Nombre total de messages envoyés:", value=messagecounts[ctx.guild.id], inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def userinfo(ctx, member: discord.Member):
    embed=discord.Embed(title=f"Statistiques de {member.name}")
    embed.add_field(name="Nombre de messages envoyés:", value=messagecounts[member.id], inline=False)
    await ctx.send(embed=embed)

@bot.event
async def on_message(message):

    if message.author.id == bot.user.id:
        return

    if message.guild.id not in messagecounts.keys():
        messagecounts[message.guild.id] = 0
    messagecounts[message.guild.id] += 1

    if message.content.endswith("quoi"):
        await message.channel.send("feur")
    
    await bot.process_commands(message)

server.server()
bot.run(TOKEN)
