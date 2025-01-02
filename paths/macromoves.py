from time import sleep
from ahk import AHK

ahk = AHK()

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
        




    def equip(self, aura) -> None:
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



    
    def use(self, item) -> None:
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

        ahk.mouse_move(xsearch, ysearch)
        sleep(0.5)
        ahk.click()

        ahk.mouse_move(xclose, yclose)
        sleep(0.5)
        ahk.click()
    
    def antiafk(self, duration: int, pause: int) -> None:

        for _ in range(duration):
            ahk.click()
            sleep(pause)