import requests
from tokens import discord_token, aura, item, webhook_url
from time import sleep
import os
import keyboard
from pyautogui import screenshot
from ahk import AHK
import asyncio



ahk = AHK()

running = False

class Macro:
    
    def quest(self) -> None:
        xbutton, ybutton = 36, 602 # x and y of "Quest" button
        xdaily, ydaily = 1276, 333 # x and y of "Daily" button

        xstquest, ystquest = 1388, 541
        xndquest, yndquest = 1392, 605
        xrdquest, yrdquest = 1390, 680

        xclaim, yclaim = 621, 769

        xclose, yclose = 1412, 297

        ahk.mouse_move(xbutton, ybutton) # Press "Quest"
        sleep(0.5)
        ahk.click(xbutton, ybutton)
        sleep(1.5)

        ahk.mouse_move(xdaily, ydaily) # Press "Daily"
        sleep(0.5)
        ahk.click(xdaily, ydaily)
        sleep(0.5)

        ahk.mouse_move(xstquest, ystquest) # Press on the 1st Quest
        sleep(0.5)
        ahk.click(xstquest, ystquest)
        sleep(0.5)

        ahk.mouse_move(xclaim, yclaim)
        ahk.click() # Claim 1st Quest
        sleep(0.5)

        ahk.mouse_move(xndquest, yndquest) # Press on the 2nd Quest
        sleep(0.5)
        ahk.click(xndquest, yndquest)
        sleep(0.5)

        ahk.mouse_move(xclaim, yclaim)
        ahk.click() # Claim 2nd Quest
        sleep(0.5)

        ahk.mouse_move(xrdquest, yrdquest) # Press on the 3rd Quest
        sleep(0.5)
        ahk.click()
        sleep(0.5)

        ahk.mouse_move(xclaim, yclaim)
        ahk.click() # Claim 3rd Quest
        sleep(0.5)

        ahk.mouse_move(xclose, yclose)
        ahk.click() # Close the tab
        sleep(0.5)
        




    def equip(self, aura):
        xbutton, ybutton = 38, 404
        xsearch, ysearch = 832, 364

        xaura, yaura = 817, 436
        xequip, yequip = 626, 632

        xclose, yclose = 1412, 297

        ahk.mouse_move(xbutton, ybutton)
        sleep(1.5)
        ahk.click()
        sleep(1.5)

        ahk.mouse_move(xsearch, ysearch)
        ahk.click()
        sleep(0.5)

        ahk.type(aura)
        sleep(1.5)

        ahk.mouse_move(xaura, yaura)
        ahk.click()
        sleep(0.5)

        ahk.mouse_move(xequip, yequip)
        ahk.click()
        sleep(0.5)

        ahk.mouse_move(xsearch, ysearch)
        ahk.click()
        sleep(0.5)

        ahk.mouse_move(xclose, yclose)
        ahk.click()
        sleep(0.5)



    
    def use(self, item):
        xbutton, ybutton = 39, 539
        xitems, yitems = 1268, 331

        xsearch, ysearch = 845, 366
        xitem, yitem = 838, 434

        xuse, yuse = 683, 579
        xclose, yclose = 1413, 296

        ahk.mouse_move(xbutton, ybutton)
        sleep(0.5)
        ahk.click()

        ahk.mouse_move(xitems, yitems)
        sleep(0.5)
        ahk.click()

        ahk.mouse_move(xsearch, ysearch)
        sleep(0.5)
        ahk.click()

        ahk.type(item)
        sleep(0.5)

        ahk.mouse_move(xitem, yitem)
        sleep(0.5)
        ahk.click()

        ahk.mouse_move(xuse, yuse)
        sleep(0.5)
        ahk.click()

        ahk.mouse_move(xclose, yclose)
        sleep(0.5)
        ahk.click()

class Screenshots:

    def screenquest(self):
        xbutton, ybutton = 36, 602 # x and y of "Quest" button
        xdaily, ydaily = 1276, 333 # x and y of "Daily" button

        xstquest, ystquest = 1388, 541
        xndquest, yndquest = 1392, 605
        xrdquest, yrdquest = 1390, 680


        xclose, yclose = 1412, 297

        ahk.mouse_move(xbutton, ybutton) # Press "Quest"
        sleep(0.5)
        ahk.click()
        sleep(1.5)

        ahk.mouse_move(xdaily, ydaily) # Press "Daily"
        sleep(0.5)
        ahk.click()
        sleep(0.5)

        ahk.mouse_move(xstquest, ystquest) # Press on the 1st Quest
        sleep(0.5)
        ahk.click()
        sleep(0.5)

        screenshot("screens/stquest.png")

        ahk.mouse_move(xndquest, yndquest) # Press on the 2nd Quest
        sleep(0.5)
        ahk.click()
        sleep(0.5)

        screenshot("screens/ndquest.png")

        ahk.mouse_move(xrdquest, yrdquest) # Press on the 3rd Quest
        sleep(0.5)
        ahk.click()
        sleep(0.5)

        screenshot("screens/rdquest.png")

        ahk.mouse_move(xclose, yclose)
        ahk.click() # Close the tab
        sleep(0.5)
    
    def screenstorage(self):
        xbutton, ybutton = 38, 404
        xsearch, ysearch = 832, 364

        xclose, yclose = 1412, 297

        ahk.mouse_move(xbutton, ybutton)
        sleep(1.5)
        ahk.click()
        sleep(1.5)

        ahk.mouse_move(xsearch, ysearch)
        ahk.click()
        sleep(0.5)

        screenshot("screens/aurastorage.png")

        ahk.mouse_move(xsearch, ysearch)
        ahk.click()
        sleep(0.5)

        ahk.mouse_move(xclose, yclose)
        ahk.click()
        sleep(0.5)

    def screenitems(self):
        xbutton, ybutton = 39, 539
        xitems, yitems = 1268, 331

        xsearch, ysearch = 845, 366


        xclose, yclose = 1413, 296

        ahk.mouse_move(xbutton, ybutton)
        sleep(0.5)
        ahk.click()

        ahk.mouse_move(xitems, yitems)
        sleep(0.5)
        ahk.click()

        ahk.mouse_move(xsearch, ysearch)
        sleep(0.5)
        ahk.click()

        screenshot("screens/itemstorage.png")

        ahk.mouse_move(xclose, yclose)
        sleep(0.5)
        ahk.click()





# Initialize Macro and Screenshots objects
macro = Macro()
screenshots = Screenshots()

def send_screenshot_to_webhook(filepath, description):
    with open(filepath, "rb") as file:
        payload = {
            "content": description,
            "embeds": [
                {
                    "title": description,
                    "color": 0x9966CC,  # Amethyst color
                    "image": {
                        "url": f"attachment://{filepath}"
                    }
                }
            ]
        }
        files = {
            "file": (os.path.basename(filepath), file)
        }
        response = requests.post(webhook_url, json=payload, files=files)
        if response.status_code == 204:
            print(f"Successfully sent {description} to webhook.")
        else:
            print(f"Failed to send {description} to webhook. Status code: {response.status_code}")

# Define the automation sequence
def automation_sequence():
    keyboard.wait("F1")
    macro.quest()
    sleep(30)  # Cooldown 900 seconds
    macro.equip(aura=aura)  
    sleep(30)  # Cooldown 900 seconds
    macro.use(item=item)  
    sleep(10)  # Cooldown 1800 seconds
    screenshots.screenquest()
    send_screenshot_to_webhook("screens/stquest.png", "**1st Quest**")
    send_screenshot_to_webhook("screens/ndquest.png", "**2nd Quest**")
    send_screenshot_to_webhook("screens/rdquest.png", "**3rd Quest")
    sleep(5)  # Cooldown 5 seconds
    screenshots.screenstorage()
    send_screenshot_to_webhook("screens/aurastorage.png", "**Aura Storage Screenshot**")
    sleep(5)  # Cooldown 5 seconds
    screenshots.screenitems()
    send_screenshot_to_webhook("screens/itemstorage.png", "**Item Storage Screenshot**")
    sleep(5)  # Cooldown 5 seconds

def start_automation():
    global running
    running = True
    while running:
        automation_sequence()

def stop_automation():
    global running
    running = False
    exit()


keyboard.add_hotkey("f1", start_automation())
keyboard.add_hotkey("f3", stop_automation())


