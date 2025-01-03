from time import sleep
from tokens import webhook_url, userid
from pyautogui import screenshot, position
from ahk import AHK
import json
import threading
import aiohttp, discord, os, asyncio


ahk = AHK()

def get_color():
        color = ahk.pixel_get_color(x=959, y=542)
        return color

def biome_color():
    color = ahk.pixel_get_color(x=50, y=952)
    return color

global colors
with open("jsons/auras.json", "r") as files:
    
    colors = json.load(files)
global biomes
with open("jsons/biomes.json", "r") as biomescolors:
    biomes = json.load(biomescolors)

gotbiomecolor = biome_color()   

def get_pos():
    while True:
        print(position())

async def send_aura_detection_to_webhook(filepath, name, rarity, isabove1m, color):
    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(webhook_url, session=session)
        with open(filepath, "rb") as file:
            if isabove1m == "Yes":
                await webhook.send(f"<@{int(userid)}>")
                embed = discord.Embed(
                    title=f"Detected **{name}**! **{rarity}**",
                    description=f"**Detected Color**: {color}\n **Above 1m aura?**: **{isabove1m}**",
                    color=discord.Color.dark_embed())
            else:
                embed = discord.Embed(
                    title=f"Detected **{name}**! **{rarity}**",
                    description=f"**Detected Color**: {color}\n **Above 1m aura?**: **{isabove1m}**",
                    color=discord.Color.dark_embed())
                
            file = discord.File(file, filename=os.path.basename(filepath))
            embed.set_image(url=f"attachment://{os.path.basename(filepath)}")
            await webhook.send(embed=embed, file=file)

detected = False

def reset_loop():
    global detected
    sleep(5)
    detected = False

def aura_detect():
    global detected
    while True:
        if not detected:
            gotcolor = get_color()
            for outer_key, outer_value in colors.items():
                if gotcolor == outer_value["Color"]:
                    if ahk.pixel_search((959, 542), (959, 542), gotcolor):
                        if ahk.pixel_get_color(x=323, y=512) == "0xFFFFFF" or ahk.pixel_get_color(x=506, y=824) == "0xFFFFFF":
                            print("\nWhite Screen! Reseting the loop")
                            detected = False
                            threading.Thread(target=reset_loop, daemon=True).start()
                            sleep(2)
                            print("\n Reseted!")
                            continue
                            
                        screenshot("screens/aurastar.png")

                        print(f"\nDetected {outer_value['Name']}! Color: {outer_value['Color']}, Rarity: {outer_value['Rarity']}")
                        asyncio.run(send_aura_detection_to_webhook(
                            filepath="screens/aurastar.png",
                            name=outer_value['Name'],
                            color=outer_value['Color'],
                            rarity=outer_value['Rarity'],
                            isabove1m=outer_value["isabove1m"]))
                        print("\nSend message an webhook!")
                        detected = True
                        threading.Thread(target=reset_loop, daemon=True).start()
        else:
            sleep(0.5)
