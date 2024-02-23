import logging
import os

import discord
from discord.app_commands import CommandInvokeError
from discord.ext import commands
from pytube import YouTube

logger = logging.getLogger("discord")


@commands.command("yt")
async def youtube_download(ctx):
    try:
        yt = YouTube(ctx.message.content[4:])
        file = yt.streams.first().download()
        logger.info(f"Successfully downloaded: {file.title()}.")
        await ctx.send(file=discord.File(file.title()))
        delete_file(file.title())
    except CommandInvokeError:
        await ctx.send("")


def delete_file(file_name: str):
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        print("The file does not exist")


async def setup(bot):
    bot.add_command(youtube_download)
