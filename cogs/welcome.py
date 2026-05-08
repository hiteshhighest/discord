import discord
from discord.ext import commands

WELCOME_CHANNEL = "welcome"


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(
            member.guild.text_channels,
            name=WELCOME_CHANNEL
        )

        if channel:
            embed = discord.Embed(
                title="Welcome!",
                description=f"Welcome to the server, {member.mention}!",
                color=discord.Color.green()
            )

            embed.set_thumbnail(url=member.display_avatar.url)

            await channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Welcome(bot))
