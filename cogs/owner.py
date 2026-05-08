from discord.ext import commands
from config import OWNER_ID


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def reload(self, ctx, extension):
        if ctx.author.id != OWNER_ID:
            return

        await self.bot.reload_extension(f"cogs.{extension}")

        await ctx.send(f"Reloaded {extension}")


async def setup(bot):
    await bot.add_cog(Owner(bot))
