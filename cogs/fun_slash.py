import discord
from discord import app_commands
from discord.ext import commands
import random


class FunSlash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="coinflip", description="Flip a coin")
    async def coinflip(self, interaction: discord.Interaction):

        result = random.choice(["Heads", "Tails"])

        embed = discord.Embed(
            title="🪙 Coin Flip",
            description=f"It landed on **{result}**",
            color=discord.Color.gold()
        )

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="dice", description="Roll a dice")
    async def dice(self, interaction: discord.Interaction):

        result = random.randint(1, 6)

        embed = discord.Embed(
            title="🎲 Dice Roll",
            description=f"You rolled **{result}**",
            color=discord.Color.blurple()
        )

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="8ball", description="Ask the magic 8ball")
    async def eightball(self, interaction: discord.Interaction, question: str):

        responses = [
            "Yes.", "No.", "Maybe.", "Definitely.",
            "Absolutely not.", "Ask again later."
        ]

        answer = random.choice(responses)

        embed = discord.Embed(
            title="🎱 8Ball",
            color=discord.Color.purple()
        )

        embed.add_field(name="Question", value=question, inline=False)
        embed.add_field(name="Answer", value=answer, inline=False)

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="rps", description="Rock Paper Scissors")
    async def rps(self, interaction: discord.Interaction, choice: str):

        options = ["rock", "paper", "scissors"]
        bot_choice = random.choice(options)

        choice = choice.lower()

        if choice not in options:
            return await interaction.response.send_message(
                "Choose rock, paper, or scissors."
            )

        if choice == bot_choice:
            result = "Tie!"
        elif (choice == "rock" and bot_choice == "scissors") or \
             (choice == "paper" and bot_choice == "rock") or \
             (choice == "scissors" and bot_choice == "paper"):
            result = "You win!"
        else:
            result = "You lose!"

        embed = discord.Embed(
            title="✂️ RPS",
            description=f"You: {choice}\nBot: {bot_choice}\n\n**{result}**",
            color=discord.Color.green()
        )

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="avatar", description="Show avatar")
    async def avatar(self, interaction: discord.Interaction, member: discord.Member = None):

        member = member or interaction.user

        embed = discord.Embed(
            title=f"{member.name}'s Avatar",
            color=discord.Color.blurple()
        )

        embed.set_image(url=member.display_avatar.url)

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(FunSlash(bot))
