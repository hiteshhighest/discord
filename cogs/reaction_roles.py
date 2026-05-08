import discord
from discord.ext import commands


class ReactionRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reactionrole(self, ctx, role: discord.Role, emoji):
        embed = discord.Embed(
            title="Reaction Roles",
            description=f"React with {emoji} to get {role.mention}",
            color=discord.Color.blurple()
        )

        msg = await ctx.send(embed=embed)
        await msg.add_reaction(emoji)


async def setup(bot):
    await bot.add_cog(ReactionRoles(bot))
