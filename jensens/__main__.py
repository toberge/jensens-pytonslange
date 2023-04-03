import os
import random

import dotenv
import discord
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.user import User

import jensens.emoji as emoji

dotenv.load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


class Roll(commands.Converter):
    async def convert(self, ctx: Context, argument):
        # TODO error
        heck = argument.split("d")
        if len(heck) == 2:
            amount = int(heck[0])
        else:
            amount = 1
        die = int(heck[0])
        rolls = [random.randint(1, die) for _ in range(amount)]
        return f":game_die: {' '.join(str(i) for i in rolls)} {emoji.equal} **{sum(rolls)}**"


@bot.command()
async def hug(ctx: Context, user: User):
    await ctx.send(f"**{ctx.author.display_name}** ga en klem til **{user.name}**")


@bot.command()
async def cat(ctx: Context):
    await ctx.send(
        "En katt til demses:",
        # embed=Embed(description="katt", url="https://cataas.com/cat", type="image"),
        embed=Embed(
            description="hvorfor må det være en beskrivelse her rph på hodet",
            type="image",
            url="https://cdn.discordapp.com/attachments/850373438236655689/850492623172665364/unknown.png",
        ),
    )


@bot.command()
async def roll(ctx: Context, argument: Roll):
    await ctx.send(argument)


# TODO hide token plz
bot.run(token=os.environ["DISCORD_TOKEN"])
