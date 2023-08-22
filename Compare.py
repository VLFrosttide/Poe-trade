import pyautogui
from pynput.keyboard import Key, Listener
import time
import pyperclip
import sys
import math
from Currency import CurrencyList
pyautogui.FAILSAFE = True 
pyautogui.MINIMUM_SLEEP = 0
pyautogui.MINIMUM_DURATION = 0.01

def add_from_invetory():
    pyautogui.keyDown("ctrl")
    pyautogui.click(x=1720,y=810)
    pyautogui.click(x=1720,y=880)
    pyautogui.click(x=1720,y=940)
    pyautogui.click(x=1720,y=1010)
    pyautogui.click(x=1720,y=1080)
##
    pyautogui.click(x=1721,y=810)
    pyautogui.click(x=1721,y=880)
    pyautogui.click(x=1721,y=940)
    pyautogui.click(x=1721,y=1010)
    pyautogui.click(x=1721,y=1080)

#    
    pyautogui.click(x=1800,y=810)
    pyautogui.click(x=1800,y=880)
    pyautogui.click(x=1800,y=940)
    pyautogui.click(x=1800,y=1010)
    pyautogui.click(x=1800,y=1080)
##
    pyautogui.click(x=1801,y=810)
    pyautogui.click(x=1801,y=880)
    pyautogui.click(x=1801,y=940)
    pyautogui.click(x=1801,y=1010)
    pyautogui.click(x=1801,y=1080)

#
    pyautogui.click(x=1870,y=810)
    pyautogui.click(x=1870,y=880)
    pyautogui.click(x=1870,y=940)
    pyautogui.click(x=1870,y=1010)
    pyautogui.click(x=1870,y=1080)
##
    pyautogui.click(x=1871,y=810)
    pyautogui.click(x=1871,y=880)
    pyautogui.click(x=1871,y=940)
    pyautogui.click(x=1871,y=1010)
    pyautogui.click(x=1871,y=1080)
#
    pyautogui.click(x=1940,y=810)
    pyautogui.click(x=1940,y=880)
    pyautogui.click(x=1940,y=940)
    pyautogui.click(x=1940,y=1010)
    pyautogui.click(x=1940,y=1080)
##
    pyautogui.click(x=1941,y=810)
    pyautogui.click(x=1941,y=880)
    pyautogui.click(x=1941,y=940)
    pyautogui.click(x=1941,y=1010)
    pyautogui.click(x=1941,y=1080)
#    
    pyautogui.click(x=2010,y=810)
    pyautogui.click(x=2010,y=880)
    pyautogui.click(x=2010,y=940)
    pyautogui.click(x=2010,y=1010)
    pyautogui.click(x=2010,y=1080)
##
    pyautogui.click(x=2011,y=810)
    pyautogui.click(x=2011,y=880)
    pyautogui.click(x=2011,y=940)
    pyautogui.click(x=2011,y=1010)
    pyautogui.click(x=2011,y=1080)
#
    pyautogui.click(x=2080,y=810)
    pyautogui.click(x=2080,y=880)
    pyautogui.click(x=2080,y=940)
    pyautogui.click(x=2080,y=1010)
    pyautogui.click(x=2080,y=1080)
#
    pyautogui.click(x=2081,y=810)
    pyautogui.click(x=2081,y=880)
    pyautogui.click(x=2081,y=940)
    pyautogui.click(x=2081,y=1010)
    pyautogui.click(x=2081,y=1080)
##
    pyautogui.click(x=2150,y=810)
    pyautogui.click(x=2150,y=880)
    pyautogui.click(x=2150,y=940)
    pyautogui.click(x=2150,y=1010)
    pyautogui.click(x=2150,y=1080)
##
    pyautogui.click(x=2151,y=810)
    pyautogui.click(x=2151,y=880)
    pyautogui.click(x=2151,y=940)
    pyautogui.click(x=2151,y=1010)
    pyautogui.click(x=2151,y=1080)

#
    pyautogui.click(x=2220,y=810)
    pyautogui.click(x=2220,y=880)
    pyautogui.click(x=2220,y=940)
    pyautogui.click(x=2220,y=1010)
    pyautogui.click(x=2220,y=1080)
##
    pyautogui.click(x=2221,y=810)
    pyautogui.click(x=2221,y=880)
    pyautogui.click(x=2221,y=940)
    pyautogui.click(x=2221,y=1010)
    pyautogui.click(x=2221,y=1080)
#
    pyautogui.click(x=2290,y=810)
    pyautogui.click(x=2290,y=880)
    pyautogui.click(x=2290,y=940)
    pyautogui.click(x=2290,y=1010)
    pyautogui.click(x=2290,y=1080)
##
    pyautogui.click(x=2291,y=810)
    pyautogui.click(x=2291,y=880)
    pyautogui.click(x=2291,y=940)
    pyautogui.click(x=2291,y=1010)
    pyautogui.click(x=2291,y=1080)

#
    pyautogui.click(x=2360,y=810)
    pyautogui.click(x=2360,y=880)
    pyautogui.click(x=2360,y=940)
    pyautogui.click(x=2360,y=1010)
    pyautogui.click(x=2360,y=1080)
##
    pyautogui.click(x=2361,y=810)
    pyautogui.click(x=2361,y=880)
    pyautogui.click(x=2361,y=940)
    pyautogui.click(x=2361,y=1010)
    pyautogui.click(x=2361,y=1080)
#
    pyautogui.click(x=2430,y=810)
    pyautogui.click(x=2430,y=880)
    pyautogui.click(x=2430,y=940)
    pyautogui.click(x=2430,y=1010)
    pyautogui.click(x=2430,y=1080)
##
    pyautogui.click(x=2431,y=810)
    pyautogui.click(x=2431,y=880)
    pyautogui.click(x=2431,y=940)
    pyautogui.click(x=2431,y=1010)
    pyautogui.click(x=2431,y=1080)
#
    pyautogui.click(x=2500,y=810)
    pyautogui.click(x=2500,y=880)
    pyautogui.click(x=2500,y=940)
    pyautogui.click(x=2500,y=1010)
    pyautogui.click(x=2500,y=1080)
##
    pyautogui.click(x=2501,y=810)
    pyautogui.click(x=2501,y=880)
    pyautogui.click(x=2501,y=940)
    pyautogui.click(x=2501,y=1010)
    pyautogui.click(x=2501,y=1080)



    #for i in range(5):
     #   for j in range(12):
    #        v = [start_y+add*i, start_y+add*(i+1)]
   #         h = [start_x+add*j, start_x+add*(j+1)]
  #          pyautogui.click((h[0]+h[1])//2, (v[0]+v[1])//2-10, duration=0.15)
    # pyautogui.keyUp("ctrl")


def hover_traders(start_x, start_y, add):
    for i in range(5):
        for j in range(12):
            v = [start_y+add*i, start_y+add*(i+1)]
            h = [start_x+add*j, start_x+add*(j+1)]
            pyautogui.moveTo((h[0]+h[1])//2, (v[0]+v[1])//2-10, duration=0.0001)



def parse_clip(clip):
    print(clip, "awdddddddddddddddddddd")
    if len(clip) == 0:
    
        return None
    lines = clip.split("\n")
    item = lines[2].strip().replace(" ", "")
    count = int(lines[4].replace("Stack Size: ", "").split("/")[0])

    return {"item":item, "count":count}

def green_check_pyautogui():
    pix = pyautogui.pixel(1255,605)
    return pix[1] == 44


def scan_inventory(start_x, start_y, add, required, debug=False):
    name, stash = next(iter(required.items()))
    for i in CurrencyList:
        if i.name == name:
            cell_count = math.ceil(stash/i.base)

    final_count = {}
    stop = False
    pyperclip.copy("")
    for i in range(12):
        if stop:
            break
        for j in range(5):
            cell_count -= 1
            v = [start_y+add*j, start_y+add*(j+1)]
            h = [start_x+add*i, start_x+add*(i+1)]
            pyautogui.moveTo((h[0]+h[1])//2, (v[0]+v[1])//2-10)
            time.sleep(0.1)
            pyautogui.click()
            
            while(pyperclip.paste()==""):
                if debug: 
                    print(f"clipboard empty!")

                greenDetected = green_check_pyautogui()
                if greenDetected and cell_count <=0:
                    if debug:
                        print("Green detected")
                    stop = True
                    break
                pyautogui.keyDown("ctrl")
                pyautogui.press("c")
                pyautogui.keyUp("ctrl")
                time.sleep(0.1)
            if stop:
                break
            clip_text = pyperclip.paste()
            if debug: 
                print(clip_text)
            cell_data = parse_clip(clip_text)
            if debug: 
                print(f"\n({i}, {j}) -> {cell_data}")
                print(f"Remaining Cell count --> {cell_count}\n")

            pyperclip.copy("")
            if cell_data["item"] in final_count:
                final_count[cell_data["item"]] += cell_data["count"] 
            else:
                final_count[cell_data["item"]] = cell_data["count"]
    

    if debug: 
        print(f"Final Count data: {final_count}")

    intersection = dict(final_count.items() & required.items())
    if len(intersection) == len(required):
        return True
    else:
        return False

"""
CurrencyType 
Quant = 100



"""

def test_run():
    def test(key):
        if key == Key.f1:
        
            start_x = 416
            start_y = 273
            Quant = 20
            Name = "Chaos Orb"
            
            result = scan_inventory(start_x,start_y,70,{Name:Quant}, True)
            print(result)
            return False
    
        with Listener(on_press = test) as listener:  
            listener.join()

if __name__ == "__main__":
    # test_run()
    
    start_x = 416
    start_y = 273
    Quant = int(sys.argv[1])
    Name = sys.argv[2]

    
    result = scan_inventory(start_x,start_y,70,{Name:Quant})
    print(result, flush=True)
