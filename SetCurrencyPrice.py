import Pricing  
from Currency import *
import sys
import pyautogui
import math
import cv2


values = sys.argv[2]
values = list(map(float, values.split()))



def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

def ChaosPrice(args):
    pyautogui.moveTo(args[0])
    pyautogui.rightClick(args[0])
    pyautogui.moveTo(args[0][0] - 200, args[0][1]+110,0.2)
    pyautogui.click(args[0][0] - 200, args[0][1]+110)
    pyautogui.moveTo(args[0][0] - 225, args[0][1]+220,0.2)
    pyautogui.click(args[0][0] - 225, args[0][1]+220)
    pyautogui.moveTo(args[0][0] - 25, args[0][1]+125,0.2)
    pyautogui.click(args[0][0] - 25, args[0][1]+125)
    pyautogui.press("backspace")
    pyautogui.press("backspace")
    pyautogui.press("backspace")
    pyautogui.press("backspace")
    pyautogui.press("backspace")
    pyautogui.press("delete")
    pyautogui.press("delete")
    pyautogui.press("delete")
    pyautogui.press("delete")
    pyautogui.press("delete")
    pyautogui.write(str( round_up(args[1], 2)))
    pyautogui.moveTo(args[0][0] + 300, args[0][1]+165)
    pyautogui.click(args[0][0] + 300, args[0][1]+165)
    
args = ()
def ChaosOrb(args):
    pyautogui.moveTo(args[0])
    pyautogui.rightClick(args[0][0], args[0][1])
    pyautogui.moveTo(args[0][0] - 200, args[0][1]+110,0.2)
    pyautogui.click(args[0][0] - 200, args[0][1]+110)
    pyautogui.moveTo(args[0][0] - 225, args[0][1]+220,0.2)
    pyautogui.click(args[0][0] - 225, args[0][1]+220)
    pyautogui.moveTo(args[0][0] - 25, args[0][1]+125,0.2)
    pyautogui.click(args[0][0] - 25, args[0][1]+125)
    pyautogui.press("backspace")
    pyautogui.press("backspace")
    pyautogui.press("backspace")
    pyautogui.press("backspace")
    pyautogui.press("backspace")
    pyautogui.press("delete")
    pyautogui.press("delete")
    pyautogui.press("delete")
    pyautogui.press("delete")
    pyautogui.press("delete")

    pyautogui.write(f"1/{args[1]}")

    #Dropdown currency type
    pyautogui.moveTo(args[0][0] + 50, args[0][1]+105)   
    pyautogui.click(args[0][0] + 50, args[0][1]+105)
    #Choose currency type
    pyautogui.moveTo(args[0][0] + 100, args[0][1]+405)   
    pyautogui.click(args[0][0] + 100, args[0][1]+405)
    pyautogui.press("enter")

    # pyautogui.moveTo(args[0][0] + 300, args[0][1]+165)
    # pyautogui.click(args[0][0] + 300, args[0][1]+165)


a = Pricing.POE("Sanctum", "Currency")
a = a.MyList()

image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
image = image[0:1440, 0:2560]

for i in range (len(CurrencyList)):
    sub = 28
    cord = CurrencyList[i].StashLocation
    img = image[cord[1]-sub:cord[1]+sub, cord[0]-sub:cord[0]+sub]
    if np.average(img) < 30:
        continue

    for j in a:
        print(args)

        if values[i] == 0:
            continue
        if CurrencyList[i].name == j.replace(" ", ""): 
            args = (CurrencyList[i].StashLocation, CurrencyList[i].price)
            ChaosPrice(args)
            CurrencyList[i].price = a[j]



mf = ([725,370], sys.argv[1])
ChaosOrb(mf)           
