import discord
import os
from discord.ext import commands
intents = discord.Intents.all()
client = commands.Bot(command_prefix="!" , intents=intents)
@client.event
async def on_ready():
    print(f"{client.user.name}{client.user.discriminator} is ready")
for cog in os.listdir("./cogs"):
    if cog.endswith(".py"):
        client.load_extension(f"cogs.{cog[:-3]}")
client.run("ODY4NDk3OTg1NDcyOTcwNzYz.YPwhxw.nGZlDvVVL4x-BU9TO_Qwrjj6-Tw") # put your token here