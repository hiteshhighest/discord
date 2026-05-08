from discord.ext import commands


def is_staff():
    async def predicate(ctx):
        return ctx.author.guild_permissions.manage_messages

    return commands.check(predicate)
