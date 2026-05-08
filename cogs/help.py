import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):

        embed = discord.Embed(
            title="🤖 Bot Help Menu",
            description="List of all available commands",
            color=discord.Color.blurple()
        )

        embed.add_field(
            name="🛠 Moderation",
            value=(
                "`!kick`, `!ban`, `!purge`,\n"
                "`!timeout`, `!untimeout`"
            ),
            inline=False
        )

        embed.add_field(
            name="🎮 Fun",
            value=(
                "`!coinflip`, `!dice`, `!8ball`,\n"
                "`!roast`, `!meme`, `!rps`,\n"
                "`!avatar`, `!say`"
            ),
            inline=False
        )

        embed.add_field(
            name="📊 Leveling",
            value="`!rank`, `!leaderboard`",
            inline=False
        )

        embed.add_field(
            name="🧰 Utility",
            value="`!ping`, `!serverinfo`, `!botinfo`",
            inline=False
        )

        embed.add_field(
            name="🎫 Tickets",
            value="`!ticketpanel`",
            inline=False
        )

        embed.add_field(
            name="👑 Owner",
            value="`!reload <cog>`",
            inline=False
        )

        embed.set_footer(text="Use commands with ! prefix")

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Help(bot))
