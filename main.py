import discord
from discord.ext import commands
import os
import asyncio

from config import TOKEN, PREFIX
from database.database import setup_database

intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix=PREFIX,
    intents=intents,
    help_command=None
)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    await bot.tree.sync()

    activity = discord.Activity(
        type=discord.ActivityType.watching,
        name="Dev - Bot!?"
    )

    await bot.change_presence(activity=activity)


async def load_extensions():
    for filename in os.listdir("./cogs"):

        if filename.endswith(".py"):

            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"Loaded {filename}")

            except Exception as e:
                print(f"Failed to load {filename}")
                print(e)


async def main():
    async with bot:

        # Setup database
        await setup_database()

        # Load cogs
        await load_extensions()

        # Start bot
        await bot.start(TOKEN)


asyncio.run(main())
