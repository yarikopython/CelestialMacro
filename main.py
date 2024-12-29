from tokens import aura, item, webhook_url
from config import settings, item_schedule, config
from paths.macropaths import Macro
from paths.macroscreenshots import Screenshots
from time import sleep
import os
import sys, subprocess
import keyboard
from pyautogui import screenshot
import aiohttp
import discord

from ahk import AHK
import asyncio
import threading


running = False

# Initialize Macro and Screenshots objects
macro = Macro()
screenshots = Screenshots()

async def send_screenshot_to_webhook(filepath, description):
    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(webhook_url, session=session)
        with open(filepath, "rb") as file:
            embed = discord.Embed(title=description, color=discord.Color.from_rgb(153, 102, 204))  # Amethyst color
            file = discord.File(file, filename=os.path.basename(filepath)) #making object of image for discord Embed
            embed.set_image(url=f"attachment://{os.path.basename(filepath)}") # setting the screenshot at embed
            await webhook.send(embed=embed, file=file) # sending embed with screenshot
        




# macro thread, that runs all of functions
def macro_thread():
    config.read("items_schedule.ini")
    keyboard.wait("F1") # waiting until the F1 button is pressed
    while True:
        macro.quest()
        macro.equip(aura=aura)
        for section in config.sections(): #getting section (its only one)
            for item, cd in config.items(section=section): #getting items and cd
                macro.use(item=item) # using items
                sleep(int(cd)) # cooldown
        
        macro.antiafk(6, 50)
        screenshots.screenquest()
        asyncio.run(send_screenshot_to_webhook("screens/quests.png", "**Quests Screenshot**"))
        sleep(5)  # Cooldown 5 seconds
        screenshots.screenstorage()
        asyncio.run(send_screenshot_to_webhook("screens/aurastorage.png", "**Aura Storage Screenshot**"))
        sleep(5)  # Cooldown 5 seconds
        screenshots.screenitems()
        asyncio.run(send_screenshot_to_webhook("screens/itemstorage.png", "**Item Storage Screenshot**"))
        sleep(5)  # Cooldown 5 seconds
        screenshots.biomelogs()
        asyncio.run(send_screenshot_to_webhook("screens/biomelogs.png", "**Biome Logs**"))
        sleep(300)


def start_thread():
    global running
    running = True
    while running:
        macro_thread()




def monitor_stop_key():
    global running
    while True:
        if keyboard.is_pressed('F3'):
            if running:
                os._exit(0)
        sleep(0.1)

def run():
    monitor = threading.Thread(target=monitor_stop_key)
    macrorun = threading.Thread(target=start_thread)

    monitor.start()
    macrorun.start()

    monitor.join()
    macrorun.join()

while True:
    os.system("cls")
    print("\nWelcome to Celestial Macro VIP+ version.")
    print("\n[1] - Run Macro")
    print("\n[2] - Item Schedule")
    print("\n[3] - Settings")
    print("\n[0] - Exit")

    choice = int(input("\nWhat you want to choose?: "))

    match choice:
        
        case 1:
            print("\n Press F1 to start macro, and F3 to stop it")
            run()
            while True:
                sleep(0.1)
        case 2:
            os.system("cls")
            item_schedule()
            sleep(5)
            os.system("cls")
        
        case 3:
            settings()
        
        case 0:
            os._exit(0)
        
        case _:
            print("Unknown option.")
            sleep(5)