from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands.context import Context
from discord.user import User


class Social(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["klem"])
    async def hug(self, ctx: Context, user: User):
        await ctx.send(
            f"**{ctx.author.display_name}** ga **{user.display_name}** en klem (づ｡◕‿‿◕｡)づ"
        )

    @commands.command(aliases=["beskyld"])
    async def blame(self, ctx: Context, user: User):
        await ctx.send(f"**{user.display_name}** har skylda 😤")

    @commands.command(aliases=["foreslå"])
    async def suggest(self, ctx: Context):
        await ctx.message.add_reaction("✅")
        await ctx.message.add_reaction("❎")


async def setup(bot: Bot):
    await bot.add_cog(Social(bot))
