"""
Taken from https://gist.github.com/EvieePy/7822af90858ef65012ea500bcecf1612
Adjusted for our context (and async setup)
"""

import sys
import traceback

import discord
from discord.ext import commands
from discord.ext.commands.context import Context

from jensens import emoji


class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: Context, error: Exception):
        # This prevents any commands with local handlers being handled here in on_command_error.
        if hasattr(ctx.command, "on_error"):
            return

        # This prevents any cogs with an overwritten cog_command_error being handled here.
        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = (commands.CommandNotFound,)

        # Allows us to check for original exceptions raised and sent to CommandInvokeError.
        # If nothing is found. We keep the exception passed to on_command_error.
        error = getattr(error, "original", error)

        # Anything in ignored will return and prevent anything happening.
        if isinstance(error, ignored):
            return

        if isinstance(error, commands.DisabledCommand):
            await ctx.send(f"{ctx.command} er deaktivert")

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send(f"{ctx.command} funker ikke i PMs {emoji.bonk}")
            except discord.HTTPException:
                pass

        elif isinstance(error, commands.BadArgument):
            # Check ctx.command.qualified_name for specific commands (if needed)
            await ctx.send(f"Ugyldig argument {emoji.bonk} ({error})")
        else:
            # All other Errors not returned come here. And we can just print the default TraceBack.
            print(f"Ignoring exception in command {ctx.command}:", file=sys.stderr)
            traceback.print_exception(
                type(error), error, error.__traceback__, file=sys.stderr
            )


async def setup(bot):
    await bot.add_cog(ErrorHandler(bot))
