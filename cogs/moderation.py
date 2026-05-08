import discord
from discord.ext import commands
from utils.embeds import success_embed, error_embed
import asyncio


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No reason provided"):
        await member.kick(reason=reason)

        await ctx.send(
            embed=success_embed(
                f"Kicked {member} | {reason}"
            )
        )

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No reason provided"):
        await member.ban(reason=reason)

        await ctx.send(
            embed=success_embed(
                f"Banned {member} | {reason}"
            )
        )

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)

        msg = await ctx.send(
            embed=success_embed(
                f"Deleted {amount} messages"
            )
        )

        await asyncio.sleep(3)
        await msg.delete()

    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def timeout(self, ctx, member: discord.Member, minutes: int, *, reason="No reason"):
        duration = discord.utils.utcnow() + discord.timedelta(minutes=minutes)

        await member.timeout(duration, reason=reason)

        await ctx.send(
            embed=success_embed(
                f"Timed out {member} for {minutes} minutes"
            )
        )

    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def untimeout(self, ctx, member: discord.Member):
        await member.timeout(None)

        await ctx.send(
            embed=success_embed(
                f"Removed timeout from {member}"
            )
        )


async def setup(bot):
    await bot.add_cog(Moderation(bot))
