import discord
from discord.ext import commands
from tokens import discord_token
from time import sleep
from ahk import AHK

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

ahk = AHK()


class Macro:
    
    def quest(self):
        pass

    def equip(self, aura):
        pass
    
    def use(self, item):
        pass