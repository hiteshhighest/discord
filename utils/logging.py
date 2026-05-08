import discord
from datetime import datetime


async def send_log(
    guild: discord.Guild,
    title: str,
    description: str,
    color=discord.Color.blurple()
):

    log_channel = discord.utils.get(
        guild.text_channels,
        name="logs"
    )

    if not log_channel:
        return

    embed = discord.Embed(
        title=title,
        description=description,
        color=color,
        timestamp=datetime.utcnow()
    )

    embed.set_footer(
        text=f"Guild ID: {guild.id}"
    )

    await log_channel.send(embed=embed)
