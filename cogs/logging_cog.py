import discord
from discord.ext import commands

LOG_CHANNEL_NAME = "logs"


class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def get_log_channel(self, guild):
        return discord.utils.get(guild.text_channels, name=LOG_CHANNEL_NAME)

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        channel = await self.get_log_channel(guild)

        if channel:
            embed = discord.Embed(
                title="Member Banned",
                description=f"{user} was banned.",
                color=discord.Color.red()
            )

            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            return

        channel = await self.get_log_channel(message.guild)

        if channel:
            embed = discord.Embed(
                title="Message Deleted",
                description=message.content,
                color=discord.Color.orange()
            )

            embed.add_field(name="Author", value=message.author)
            embed.add_field(name="Channel", value=message.channel.mention)

            await channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Logging(bot))
