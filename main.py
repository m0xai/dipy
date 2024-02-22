import os
from urllib.parse import urlparse

import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

app_token = os.getenv("DISCORD_APP_TOKEN")

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(">", intents=intents)


@bot.command("ping")
async def pong(ctx):
    await ctx.send("pong")


@bot.command("ig")
async def download_insta_media(ctx):
    channel = bot.get_channel(ctx.message.channel.id)
    video_url_msg = ctx.message.content[4:]

    parsed_url = urlparse(video_url_msg)
    base_url = "{uri.scheme}://{uri.netloc}".format(uri=parsed_url)
    exact_url = base_url + parsed_url.path
    download_url = exact_url + "?__a=1&__d=dis"

    video_url_req = requests.get(download_url).json()
    video_url = video_url_req["graphql"]["shortcode_media"]["video_url"]

    await save_video(video_url)
    await channel.send(file=discord.File("file.mp4"))


async def save_video(url):
    response = requests.get(url)
    with open("file.mp4", "wb") as file:
        file.write(response.content)
    return file


bot.run(app_token)
