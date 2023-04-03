from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands.context import Context


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def github(self, ctx: Context):
        await ctx.send(
            "",
            embed=Embed(
                title="Kildekoden finner du her:",
                description="[github.com/toberge/jensens-pytonslange](https://github.com/toberge/jensens-pytonslange)",
            ),
        )

    @commands.command()
    async def about(self, ctx: Context):
        embed = Embed(
            title="Jensens rørleggerservice",
            description="Vi leverer bare rør. Les mer [her](https://rørleggerjensen.no/).",
        )
        embed.set_thumbnail(
            url="https://files.solvecms.com/test/7311e68/medium/jensen%20r%C3%B8rleggerservice%20logo.jpg?v=1519740759023"
        )
        embed.set_image(
            url="https://files.solvecms.com/test/7311e68/medium/jensen%20r%C3%B8rleggerservice%20logo.jpg?v=1519740759023"
        )
        embed.add_field(name="Stiftet", value="2014")
        embed.add_field(name="Vi tilbyr", value="rørlegging og sånt")
        await ctx.send(
            "",
            embed=embed,
        )


async def setup(bot: Bot):
    await bot.add_cog(Info(bot))
