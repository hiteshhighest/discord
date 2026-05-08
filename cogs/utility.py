import discord
from discord.ext import commands
import platform


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.command()
    async def serverinfo(self, ctx):
        guild = ctx.guild

        embed = discord.Embed(
            title=guild.name,
            color=discord.Color.blurple()
        )

        embed.add_field(name="Members", value=guild.member_count)
        embed.add_field(name="Owner", value=guild.owner)

        await ctx.send(embed=embed)

    @commands.command()
    async def botinfo(self, ctx):
        embed = discord.Embed(
            title="Bot Info",
            color=discord.Color.green()
        )

        embed.add_field(name="Python", value=platform.python_version())
        embed.add_field(name="discord.py", value=discord.__version__)

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Utility(bot))
