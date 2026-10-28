import os
import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = discord.Object(id=int(os.getenv("GUILD_ID")))

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name="ping", description="ทดสอบบอท", guild=GUILD)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong!")

@client.event
async def on_ready():
    await tree.sync(guild=GUILD)
    print(f"ล็อกอินเป็น {client.user}")

client.run(TOKEN)

