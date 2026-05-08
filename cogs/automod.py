import discord
from discord.ext import commands

BAD_WORDS = [
    "badword1",
    "badword2"
]


class AutoMod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        content = message.content.lower()

        if any(word in content for word in BAD_WORDS):
            await message.delete()

            await message.channel.send(
                f"{message.author.mention}, inappropriate language is not allowed.",
                delete_after=5
            )

        links = ["http://", "https://", "discord.gg"]

        if any(link in content for link in links):
            if not message.author.guild_permissions.manage_messages:
                await message.delete()

                await message.channel.send(
                    f"{message.author.mention}, links are not allowed.",
                    delete_after=5
                )


async def setup(bot):
    await bot.add_cog(AutoMod(bot))
