# bot.py

import os
import discord
from discord.ext import commands
from ffmpeg_handler import start_recording, stop_recording, is_recording

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send(f"👋 Hello, {ctx.author.display_name}! I'm ready to record your stream.")

@bot.command()
async def record(ctx):
    success, message = start_recording()
    await ctx.send(message)

@bot.command()
async def stop(ctx):
    success, result = stop_recording()
    if success:
        try:
            await ctx.send("🟢 Recording stopped. Uploading...", file=discord.File(result))
        except discord.HTTPException:
            await ctx.send("📁 Recording too large to upload. File saved locally.")
    else:
        await ctx.send(result)

@bot.command()
async def status(ctx):
    if is_recording():
        await ctx.send("🔴 Recording is currently running.")
    else:
        await ctx.send("🟢 No recording is active.")

# Run the bot
bot.run(os.getenv("DISCORD_TOKEN"))

