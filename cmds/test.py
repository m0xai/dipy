from discord.ext import commands


@commands.command("ping")
async def pong(ctx):
    await ctx.send("pong")


async def setup(bot):
    bot.add_command(pong)
