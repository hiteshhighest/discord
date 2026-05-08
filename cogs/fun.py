import discord
from discord.ext import commands
import random


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.eight_ball_responses = [
            "Yes.",
            "No.",
            "Maybe.",
            "Definitely.",
            "Absolutely not.",
            "Ask again later.",
            "Most likely.",
            "I don't think so.",
            "Without a doubt.",
            "Very doubtful."
        ]

    @commands.command()
    async def coinflip(self, ctx):
        result = random.choice(["Heads", "Tails"])

        embed = discord.Embed(
            title="🪙 Coin Flip",
            description=f"The coin landed on **{result}**!",
            color=discord.Color.gold()
        )

        await ctx.send(embed=embed)

    @commands.command()
    async def dice(self, ctx):
        result = random.randint(1, 6)

        embed = discord.Embed(
            title="🎲 Dice Roll",
            description=f"You rolled a **{result}**!",
            color=discord.Color.blurple()
        )

        await ctx.send(embed=embed)

    @commands.command(aliases=["8ball"])
    async def eightball(self, ctx, *, question):
        response = random.choice(self.eight_ball_responses)

        embed = discord.Embed(
            title="🎱 8Ball",
            color=discord.Color.purple()
        )

        embed.add_field(name="Question", value=question, inline=False)
        embed.add_field(name="Answer", value=response, inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def roast(self, ctx, member: discord.Member):
        roasts = [
            f"{member.mention} probably thinks Python is a snake only.",
            f"{member.mention} downloads RAM from the internet.",
            f"{member.mention} thinks turning it off and on again is hacking.",
            f"{member.mention} failed a captcha test.",
            f"{member.mention} claps when the plane lands."
        ]

        embed = discord.Embed(
            title="🔥 Roast",
            description=random.choice(roasts),
            color=discord.Color.red()
        )

        await ctx.send(embed=embed)

    @commands.command()
    async def meme(self, ctx):
        memes = [
            "https://i.imgur.com/8Km9tLL.jpg",
            "https://i.imgur.com/sJ3CT4V.gif",
            "https://i.imgur.com/dJa0Hpl.jpg"
        ]

        embed = discord.Embed(
            title="😂 Meme",
            color=discord.Color.random()
        )

        embed.set_image(url=random.choice(memes))

        await ctx.send(embed=embed)

    @commands.command()
    async def rps(self, ctx, choice):
        options = ["rock", "paper", "scissors"]

        bot_choice = random.choice(options)
        choice = choice.lower()

        if choice not in options:
            return await ctx.send(
                "Choose either: rock, paper, or scissors."
            )

        if choice == bot_choice:
            result = "It's a tie!"
        elif (
            (choice == "rock" and bot_choice == "scissors")
            or (choice == "paper" and bot_choice == "rock")
            or (choice == "scissors" and bot_choice == "paper")
        ):
            result = "You win!"
        else:
            result = "You lose!"

        embed = discord.Embed(
            title="✂️ Rock Paper Scissors",
            color=discord.Color.green()
        )

        embed.add_field(name="Your Choice", value=choice.capitalize())
        embed.add_field(name="Bot Choice", value=bot_choice.capitalize())
        embed.add_field(name="Result", value=result, inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        member = member or ctx.author

        embed = discord.Embed(
            title=f"{member.name}'s Avatar",
            color=discord.Color.blurple()
        )

        embed.set_image(url=member.display_avatar.url)

        await ctx.send(embed=embed)

    @commands.command()
    async def say(self, ctx, *, message):
        await ctx.message.delete()

        embed = discord.Embed(
            description=message,
            color=discord.Color.blurple()
        )

        embed.set_footer(text=f"Sent by {ctx.author}")

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Fun(bot))
