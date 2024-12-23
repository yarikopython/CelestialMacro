import discord
from discord.ext import commands
from tokens import discord_token

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

