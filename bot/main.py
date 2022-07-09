import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import os

intents = discord.Intents.all()
client = commands.Bot(command_prefix="?", intents=intents,
                      case_insensetive=True)
TOKEN = os.getenv("DISCORD_TOKEN")

@client.event
async def on_ready():
    print('Bot successfully started')
    await client.change_presence(activity=discord.Game(name="{0} - prefix".format("?")))


@client.command()
@has_permissions(administrator=True)
async def load(ctx, ext):
    client.load_extension(f'cogs.{ext}')
    print(f"{ext} loaded")


@client.command()
@has_permissions(administrator=True)
async def unload(ctx, ext):
    client.unload_extension(f'cogs.{ext}')
    print(f"{ext} unloaded")


@client.command()
@has_permissions(administrator=True)
async def reload(ctx, ext):
    client.unload_extension(f'cogs.{ext}')
    client.load_extension(f'cogs.{ext}')
    print(f"{ext} reloaded")

@client.command()
@has_permissions(administrator=True)
async def unloadall(ctx):
    for filename in os.listdir('bot/cogs'):
        if filename.endswith('.py'):
            client.unload_extension(f'cogs.{filename[:-3]}')
    print('Everything is unloaded now')

@client.command()
@has_permissions(administrator=True)
async def loadall(ctx):
    for filename in os.listdir('bot/cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')

for filename in os.listdir('bot/cogs'):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(TOKEN)
