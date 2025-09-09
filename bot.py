from discord.ext import commands, tasks
import discord
from tipbot.tips import generate_tip
from tipbot.config import DISCORD_BOT_TOKEN, CHANNEL_ID, TIMEZONE
import datetime as dt
from zoneinfo import ZoneInfo

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    channel = await bot.fetch_channel(CHANNEL_ID)
    await channel.send(f"Logged in as {bot.user}")
    if not tip.is_running():
        tip.start()
        print("Loop started; next at:", tip.next_iteration)


@tasks.loop(time=dt.time(hour=16, tzinfo=ZoneInfo(TIMEZONE)))
async def tip():
    channel = await bot.fetch_channel(CHANNEL_ID)
    await channel.send(f"Tip of the day: {generate_tip()}")


@tip.before_loop
async def before_tip():
    await bot.wait_until_ready()
    now = dt.datetime.now(ZoneInfo(TIMEZONE))
    print("loop armed at:", now.isoformat())

bot.run(DISCORD_BOT_TOKEN)
