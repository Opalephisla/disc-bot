import os

import discord
from discord import Client, Embed, Intents
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

import server

bot = Client(intents=Intents.default())
bot = commands.Bot(command_prefix="!")
slash = SlashCommand(bot)


@slash.slash(name="test")
async def test(ctx: SlashContext):
    embed = Embed(title="Météo à Brest")
    embed.set_author(name="OpenWeatherMap", url="https://openweathermap.org/", icon_url="https://openweathermap.org/themes/openweathermap/assets/img/logo_white_cropped.png")
    embed.set_thumbnail(url="https://france3-regions.francetvinfo.fr/image/fSinvo3WjAiD0hmMwCdczuuROE8/930x620//filters:format(webp)/regions/2020/06/09/5edee5ff39b34_vlcsnap-2015-11-26-09h51m24s0.png")

    embed.add_field(name="Température", value=str(server.get_weather_brest()["main"]["temp"]) + " °C", inline=False)
    embed.add_field(name="Humidité", value=str(server.get_weather_brest()["main"]["humidity"]) + " %", inline=False)
    embed.add_field(name="Vent", value=str(server.get_weather_brest()["wind"]["speed"]) + " noeuds", inline=False)
    embed.add_field(name="Pluie", value="Le temps sera " + str(server.get_weather_brest()["weather"][0]["description"]), inline=False)
    embed.set_footer(text="Météo actuelle pour la ville de Brest, fourni par https://openweathermap.org/")
    await ctx.send(embed=embed)

@slash.slash(name="help")
async def help(ctx: SlashContext):
    embed = Embed(title="Menu d'aide pour les commandes du bot {bot.user.name}")
    embed.add_field(name="/help", value="Permet d'afficher ce menu", inline=False)
    embed.add_field(name="/metis", value="Affiche  un lien vers la plateforme Métis de l'AFPA", inline=False)
    embed.add_field(name="/meteo", value="Renvoie la météo actuelle à Brest", inline=False)
    await ctx.send(embed=embed)


@slash.slash(name="meteo")
async def meteo(ctx: SlashContext):
    embed = Embed(title="Météo à Brest")
    embed.add_field(name="Température", value=server.get_weather_brest()[0], inline=False)
    embed.add_field(name="Humidité", value=server.get_weather_brest()[1], inline=False)
    embed.add_field(name="Vent", value=server.get_weather_brest()[2], inline=False)
    embed.add_field(name="Pluie", value=server.get_weather_brest()[3], inline=False)
    await ctx.send(embed=embed)


@slash.slash(name="metis")
async def metis(ctx: SlashContext):
    embed = Embed(title="Lien vers la plateforme Métis de l'AFPA")
    embed.add_field(name="Lien", value="https://metis.afpa.fr/", inline=False)
    await ctx.send(embed=embed)


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
    embed = discord.Embed(title=f"Statistiques du serveur {ctx.guild.name}")
    embed.add_field(name="Nombre d'utilisateurs:", value=ctx.guild.member_count, inline=False)
    embed.add_field(name="Nombres de salons:", value=len(ctx.guild.channels), inline=False)
    embed.add_field(name="Nombre total de messages envoyés:", value=messagecounts[ctx.guild.id], inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def userinfo(ctx, member: discord.Member):
    embed = discord.Embed(title=f"Statistiques de {member.name}")
    embed.add_field(name="Nombre de messages envoyés:", value=messagecounts[member.id], inline=False)
    await ctx.send(embed=embed)


@bot.event
async def on_message(message):

    await bot.process_commands(message)

    if message.author.id == bot.user.id:
        return

    if message.guild.id not in messagecounts.keys():
        messagecounts[message.guild.id] = 0
    messagecounts[message.guild.id] += 1

    if message.content.endswith("quoi"):
        await message.channel.send("feur")


server.server()

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
