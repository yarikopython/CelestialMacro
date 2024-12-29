from ahk import AHK

from pyautogui import screenshot
from time import sleep

ahk = AHK()

class Screenshots:

    def screenquest(self) -> None:
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
        ahk.click() #clicking 
        sleep(0.5)

        screenshot("screens/quests.png") # Screenshoting

        ahk.mouse_move(xclose, yclose)
        ahk.click() # Close the tab
        sleep(0.5)
    
    def screenstorage(self) -> None:
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


    def biomelogs(self) -> None:
        xbutton, ybutton = 38, 674
        xserver, yserver = 948, 645
        xclose, yclose = 1410, 315
        xtodrag, ytodrag = 1268, 448

        ahk.mouse_move(xbutton, ybutton)
        sleep(0.5)
        ahk.click()

        ahk.mouse_move(xserver, yserver)
        sleep(0.5)
        ahk.click()

        ahk.mouse_move(xtodrag, ytodrag)
        for _ in range(10):
            ahk.send_input("{WheelDown}")

        ahk.mouse_move(xclose, yclose)


        sleep(1.0)
        screenshot("screens/biomelogs.png")

        sleep(0.5)
        ahk.click()

    def screenitems(self) -> None:
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