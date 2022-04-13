import os
from threading import Thread

from flask import Flask, redirect, render_template, url_for

app = Flask("")
API_KEY = os.getenv("API_KEY")


@app.route("/")
def main():
    return render_template("index.html")


def run():
    app.run(host="0.0.0.0", port=8080)


def server():
    server = Thread(target=run)
    server.start()


# get weather for city Brest from openweathermap.org
def get_weather_brest():
    import json

    import requests

    url = "https://api.openweathermap.org/data/2.5/weather?q=Brest,fr&lang=fr&units=metric&appid=" + API_KEY
    response = requests.get(url)
    data = json.loads(response.text)
    return data
