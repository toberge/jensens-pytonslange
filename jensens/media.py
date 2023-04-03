from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands.context import Context


class Media(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["katt"])
    async def cat(self, ctx: Context):
        return await ctx.send("https://cataas.com/cat")


async def setup(bot: Bot):
    await bot.add_cog(Media(bot))
