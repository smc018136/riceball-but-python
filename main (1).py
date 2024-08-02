import os
import discord
from discord import app_commands
from discord.ext import commands
from discord import DMChannel
from discord.ext.commands import has_permissions, MissingPermissions
from keep_alive import keep_alive
from discord.ext import tasks
from itertools import cycle
import requests
import datetime
import asyncio

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
intents.members = True

status = cycle(['with Python','JetHub'])

@tasks.loop(seconds=10)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))

bot = commands.Bot(command_prefix="/", case_insensitive=True, intents=intents)
cats = ["idk", "idfk"]

@bot.event
async def on_ready():
    change_status.start()
    print("Bot is ready!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced{len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.event
async def on_message(message):
    msg = message.content

    if message.author == bot.user:
        return

    if 'fdsf' in message.content.lower():
        await message.delete()

    if 'ffff' in message.content.lower():
        await message.delete()

    if 'cat' in msg.lower():
        await message.channel.send("dfsdf")

    if 'dick' in msg.lower():
        await message.channel.send("can i suck")

@bot.tree.command(name="duck", description="idk")
async def duck(interaction: discord.Interaction):
    await interaction.response.send_message("wahhh")


keep_alive()
my_secret = os.environ['fdsfd']
bot.run(my_secret)
