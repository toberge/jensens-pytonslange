import random

from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands.context import Context

import jensens.emoji as emoji


class Dice:
    def __init__(self, definition):
        dice = definition.split("d")
        if definition.startswith("d"):
            self.amount = 1
        else:
            self.amount = int(dice[0])
        self.die = int(dice[1])

    def roll(self):
        return [random.randint(1, self.die) for _ in range(self.amount)]


class Roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["rull"])
    async def roll(self, ctx: Context, argument: Dice):
        rolls = argument.roll()
        return await ctx.send(
            f":game_die: {' + '.join(str(i) for i in rolls)} {emoji.equal} **{sum(rolls)}**"
        )


async def setup(bot: Bot):
    await bot.add_cog(Roll(bot))
