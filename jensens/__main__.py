import asyncio
import os

import dotenv
import discord
from discord.ext import commands


async def main():
    dotenv.load_dotenv()

    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    await bot.load_extension("jensens.dice")
    await bot.load_extension("jensens.media")
    await bot.load_extension("jensens.social")
    await bot.load_extension("jensens.info")
    await bot.load_extension("jensens.error")

    print("Good to go!")
    print("Modules loaded:", ", ".join([module for module in bot.extensions.keys()]))
    print("Commands:", ", ".join([command.name for command in bot.commands]))

    await bot.start(token=os.environ["DISCORD_TOKEN"])


if __name__ == "__main__":
    asyncio.run(main())
