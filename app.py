import asyncio
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

discord.utils.setup_logging()

load_dotenv()
app_token = os.getenv("DISCORD_APP_TOKEN")

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(">", intents=intents)


async def main():
    async with bot:
        await bot.load_extension("cmds.test")
        await bot.load_extension("cmds.yt_dl")
        await bot.load_extension("cmds.ig_dl")
        await bot.start(app_token)


asyncio.run(main())
