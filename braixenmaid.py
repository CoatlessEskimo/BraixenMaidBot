# bot.py
import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='#!')

@bot.command(name='helppls', aliases=['man', '?'])
async def helppls(ctx):
    await ctx.send("This bot automatically detects media.discordapp.net links and replaces them with cdn.discordapp.com links.")

@bot.listen()
async def on_message(message):
    if message.content.startswith("https://media.discordapp.net/"):
        oldLink = message.content
        newLink = oldLink.replace('media.discordapp.net', 'cdn.discordapp.com')
        sendingUser = message.author
        await message.delete()
        await message.channel.send(f"From {sendingUser} {newLink}")
    if message.content.startswith("https://youtube.com/shorts/"):
        oldLink = message.content
        newLink = oldLink.replace('shorts/', 'watch?v=')
        newestLink = newLink.replace('?feature=share', '')
        sendingUser = message.author
        await message.delete()
        await message.channel.send(f"From {sendingUser} {newestLink}")
        
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="GUILTY GEAR XX ACCENT CORE PLUS R"))

bot.run(TOKEN)
