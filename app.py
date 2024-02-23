import asyncio
import os
import sys
import traceback

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


async def on_command_error(ctx: commands.Context, error):
    # Handle your errors here
    if isinstance(error, commands.MemberNotFound):
        await ctx.send("I could not find member '{error.argument}'. Please try again")

    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"'{error.param.name}' is a required argument.")
    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send(str(error))
    else:
        # All unhandled errors will print their original traceback
        print(f"Ignoring exception in command {ctx.command}:", file=sys.stderr)
        traceback.print_exception(
            type(error), error, error.__traceback__, file=sys.stderr
        )


bot.on_command_error = on_command_error

asyncio.run(main())
