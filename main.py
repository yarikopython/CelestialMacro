from tokens import aura, webhook_url
from config import settings, item_schedule
from configparser import ConfigParser
from paths.macromoves import Macro
from auradetection import aura_detect
from paths.macroscreenshots import Screenshots
from time import sleep
import os, keyboard, aiohttp, discord, asyncio, threading, sys
from colorama import Fore, init
from ahk import AHK


init(autoreset=True)
running = False

# Initialize Macro and Screenshots objects
macro = Macro()
screenshots = Screenshots()

async def send_screenshot_to_webhook(filepath, description):
    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(url=webhook_url, session=session)
        with open(filepath, "rb") as file:
            embed = discord.Embed(title=description, color=discord.Color.from_rgb(153, 102, 204))  # Amethyst color
            file = discord.File(file, filename=os.path.basename(filepath)) #making object of image for discord Embed
            embed.set_image(url=f"attachment://{os.path.basename(filepath)}") # setting the screenshot at embed
            await webhook.send(embed=embed, file=file) # sending embed with screenshot
        



# macro thread, that runs all of functions
def macro_thread():
    config = ConfigParser()
    
    while True:
        macro.quest()
        sleep(5.0)
        macro.equip(aura=aura)
        sleep(5.0)
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
        macro.antiafk(5, 300)

def monitor_start_key():
    while True:
        if keyboard.is_pressed("F1"):
            print(Fore.GREEN + print("F1 was pressed, starting the programm."))
            macro_thread()
            while True:
                sleep(0.1)

def monitor_restart_key():
    while True:
        if keyboard.is_pressed("F2"):
            print(Fore.YELLOW + "\nF2 was pressed, restarting the programm.\n")
            os.execv(sys.executable, ['python'] + sys.argv)

def monitor_stop_key():
    while True:
        if keyboard.is_pressed('F3'):
            print(Fore.RED + "\nF3 was pressed, ending the programm.")
            os._exit(0)
        sleep(0.1)



def main():
    try:
        while True:
            os.system("cls")
            print(Fore.MAGENTA + "\nWelcome to Celestial Macro VIP+ version.")
            print(Fore.LIGHTMAGENTA_EX + "\n[1] - Information")
            print(Fore.LIGHTMAGENTA_EX + "\n[2] - Item Schedule")
            print(Fore.LIGHTMAGENTA_EX + "\n[3] - Settings")
            print(Fore.LIGHTMAGENTA_EX + "\n[0] - Exit")

            aura_detector_thread = threading.Thread(target=aura_detect)
            aura_detector_thread.start()

            f1_thread = threading.Thread(target=monitor_start_key)
            f1_thread.start()

            f2_thread = threading.Thread(target=monitor_restart_key)
            f2_thread.start()

            f3_thread = threading.Thread(target=monitor_stop_key)
            f3_thread.start()

            choice = int(input("\nWhat you want to choose?: "))

            match choice:
                
                case 1:
                    os.system("cls")
                    print(Fore.MAGENTA + "\nWelcome! This is Celestial Macro VIP+\n this macro was created for vip+ users.\n soon the GUI going be available, same as Celestial Macro (for non VIP+ users?)???")
                    sleep(5)
                    os.system("cls")
                case 2:
                    os.system("cls")
                    item_schedule()

                    print(Fore.LIGHTMAGENTA_EX + "Wait until you comeback into menu")

                    sleep(5)
                    os.system("cls")
                
                case 3:
                    settings()
                
                case 0:
                    os._exit(0)
                
                case _:
                    print(Fore.RED + "Unknown option. Please wait 5 seconds to get back into menu")
                    sleep(5)
    except KeyboardInterrupt:
        os.system("cls")
        os._exit(0)

main()