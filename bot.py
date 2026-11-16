import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ["DISCORD_TOKEN"]
CHANNEL_ID = int(os.environ["CHANNEL_ID"])

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    channel = await client.fetch_channel(CHANNEL_ID)
    await channel.send("Outage bot online.")
    print(f"Logged in as {client.user}")
    await client.close()


client.run(TOKEN)