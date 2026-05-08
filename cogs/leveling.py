import discord
from discord.ext import commands
import aiosqlite

DB_NAME = "data/levels.db"

# 🎯 LEVEL ROLE REWARDS (replace IDs with your server roles)
LEVEL_ROLES = {
    5: 1501852770435600394,
    10: 1501852996785672254,
    20: 1501853046572060792
}


class Leveling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def create_table(self):
        async with aiosqlite.connect(DB_NAME) as db:
            await db.execute(
                """
                CREATE TABLE IF NOT EXISTS levels (
                    guild_id INTEGER,
                    user_id INTEGER,
                    xp INTEGER,
                    level INTEGER
                )
                """
            )
            await db.commit()

    @commands.Cog.listener()
    async def on_ready(self):
        await self.create_table()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if not message.guild:
            return

        xp_gain = 10

        async with aiosqlite.connect(DB_NAME) as db:

            cursor = await db.execute(
                """
                SELECT xp, level FROM levels
                WHERE guild_id = ? AND user_id = ?
                """,
                (message.guild.id, message.author.id)
            )

            data = await cursor.fetchone()

            # 🆕 NEW USER
            if data is None:
                xp = xp_gain
                level = 1

                await db.execute(
                    """
                    INSERT INTO levels (guild_id, user_id, xp, level)
                    VALUES (?, ?, ?, ?)
                    """,
                    (message.guild.id, message.author.id, xp, level)
                )

            else:
                xp, level = data
                xp += xp_gain

                next_level_xp = level * 100

                leveled_up = False

                if xp >= next_level_xp:
                    level += 1
                    leveled_up = True

                    await message.channel.send(
                        f"🎉 {message.author.mention} leveled up to **Level {level}**!"
                    )

                    # 🏆 ROLE REWARD SYSTEM
                    if level in LEVEL_ROLES:

                        role = message.guild.get_role(LEVEL_ROLES[level])

                        if role:
                            await message.author.add_roles(role)

                            await message.channel.send(
                                f"🏆 {message.author.mention} earned **{role.name}** role!"
                            )

                await db.execute(
                    """
                    UPDATE levels
                    SET xp = ?, level = ?
                    WHERE guild_id = ? AND user_id = ?
                    """,
                    (
                        xp,
                        level,
                        message.guild.id,
                        message.author.id
                    )
                )

            await db.commit()

    # 📊 RANK COMMAND
    @commands.command()
    async def rank(self, ctx, member: discord.Member = None):
        member = member or ctx.author

        async with aiosqlite.connect(DB_NAME) as db:

            cursor = await db.execute(
                """
                SELECT xp, level FROM levels
                WHERE guild_id = ? AND user_id = ?
                """,
                (ctx.guild.id, member.id)
            )

            data = await cursor.fetchone()

            if data is None:
                return await ctx.send(f"{member.mention} has no XP yet.")

            xp, level = data
            next_level_xp = level * 100

            embed = discord.Embed(
                title=f"📊 {member.name}'s Rank",
                color=discord.Color.blurple()
            )

            embed.set_thumbnail(url=member.display_avatar.url)

            embed.add_field(name="Level", value=level, inline=True)
            embed.add_field(
                name="XP", value=f"{xp}/{next_level_xp}", inline=True)

            await ctx.send(embed=embed)

    # 🏆 LEADERBOARD COMMAND
    @commands.command()
    async def leaderboard(self, ctx):

        async with aiosqlite.connect(DB_NAME) as db:

            cursor = await db.execute(
                """
                SELECT user_id, xp, level
                FROM levels
                WHERE guild_id = ?
                ORDER BY xp DESC
                LIMIT 10
                """,
                (ctx.guild.id,)
            )

            data = await cursor.fetchall()

            if not data:
                return await ctx.send("No leaderboard data found.")

            embed = discord.Embed(
                title="🏆 Leaderboard",
                color=discord.Color.gold()
            )

            description = ""

            for index, (user_id, xp, level) in enumerate(data, start=1):

                member = ctx.guild.get_member(user_id)

                if member:
                    description += (
                        f"**{index}.** {member.mention} "
                        f"— Level {level} ({xp} XP)\n"
                    )

            embed.description = description

            await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Leveling(bot))
