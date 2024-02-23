import logging
from urllib.parse import urlparse

import discord
import requests
from discord.ext import commands

logger = logging.getLogger("discord")


@commands.command("ig")
async def download_insta_media(ctx):
    video_url_msg = ctx.message.content[4:]
    parsed_url = urlparse(video_url_msg)
    base_url = "{uri.scheme}://{uri.netloc}".format(uri=parsed_url)
    exact_url = base_url + parsed_url.path
    download_url = exact_url + "?__a=1&__d=dis"
    logger.info(f"Downloading video from: {download_url}.")

    video_url_req = requests.get(download_url).json()
    video_url = video_url_req["graphql"]["shortcode_media"]["video_url"]

    await save_video(video_url)
    logger.info("Video Downloaded successfully.")
    await ctx.send(file=discord.File("file.mp4"))


async def save_video(url):
    response = requests.get(url)
    with open("file.mp4", "wb") as file:
        file.write(response.content)
    return file


async def setup(bot):
    bot.add_command(download_insta_media)
