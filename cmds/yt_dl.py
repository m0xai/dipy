from discord.ext import commands


@commands.command("yt")
async def youtube_download(ctx):
    await ctx.send("pong")


async def setup(bot):
    bot.add_command(youtube_download)
