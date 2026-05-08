import discord
from config import EMBED_COLOR


def success_embed(message: str):
    return discord.Embed(
        description=f"✅ {message}",
        color=0x57F287
    )


def error_embed(message: str):
    return discord.Embed(
        description=f"❌ {message}",
        color=0xED4245
    )


def info_embed(message: str):
    return discord.Embed(
        description=message,
        color=EMBED_COLOR
    )
