import pyautogui
import time
import sys
import Pricing
from Essence import *
print("awd")
[80,244]
[620, 404]
def SetPriceFirstHalf(args):
    
    pyautogui.moveTo(args[0])
    pyautogui.rightClick(args[0])
    time.sleep(0.2)
    pyautogui.moveTo([args[0][0], args[0][1]+100])
    time.sleep(0.2)
    pyautogui.click([args[0][0] , args[0][1]+100])
    time.sleep(0.2)
    pyautogui.moveTo([args[0][0] , args[0][1]+220])
    pyautogui.click([args[0][0] , args[0][1]+220])
    time.sleep(0.2)
    pyautogui.moveTo([args[0][0] + 200, args[0][1] +100])
    pyautogui.click([args[0][0] + 200, args[0][1] + 100])
    time.sleep(0.2)
    pyautogui.press("backspace")
    time.sleep(0.2)
    pyautogui.press("backspace")
    pyautogui.press("backspace")
    time.sleep(0.2)
    pyautogui.write(str(args[1]))
    time.sleep(0.2)
    pyautogui.moveTo([args[0][0] + 540, args[0][1] + 170])
    time.sleep(0.1)
    pyautogui.click([args[0][0] + 540, args[0][1] + 170])
    time.sleep(0.2)

def Printstuff(args):
    print(args)
    print((args[0][0], args[0][1]+100))
    print(args[0][0], args[0][1]+220)
    print(args[0][0]+ 540, args[0][1] + 170)

def SetPriceSecondHalf(args):
    
    pyautogui.moveTo(args[0])
    pyautogui.rightClick(args[0])
    pyautogui.moveTo(args[0][0], args[0][1]+100)
    pyautogui.click(args[0][0] + args[0][1]+100)
    pyautogui.moveTo(args[0][0] + args[0][1]+220)
    pyautogui.click(args[0][0] + args[0][1]+220)
    pyautogui.moveTo(args[0][0] + 200, args[0][1] +100)
    pyautogui.click(args[0][0] + 200, args[0][1] + 100)
    pyautogui.write(args[1])
    pyautogui.moveTo(args[0][0] + 540, args[0][1] + 170)
    
EssenceList[0].price = 1
EssenceList[1].price = 1
EssenceList[2].price = 1
EssenceList[3].price= 1
EssenceList[4].price=1
EssenceList[5].price=1
EssenceList[6].price=1
EssenceList[7].price=1
EssenceList[8].price=1
EssenceList[9].price=1

Clickthis = ()
while True:
    print("start")
    a = Pricing.POE("Sanctum", sys.argv[1])
    a = a.get_all_essence_values()
    
    for i in range (len(EssenceList)):
        for j in a:
            if EssenceList[i].name == j.replace(" ", "") and EssenceList[i].price != a[j]:
                Clickthis = (EssenceList[i].StashLocation,int(a[j]))
                if (i<12):
                    SetPriceFirstHalf(Clickthis)
                else:
                    SetPriceSecondHalf(Clickthis)
                    
                EssenceList[i].price = a[j]
    print("finish")                
    time.sleep(900)
            

    
    
