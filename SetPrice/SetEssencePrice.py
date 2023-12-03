import pyautogui
import time
import sys
import Pricing
from Essence import *
import pyautogui
import cv2
import numpy as np
import math

values = sys.argv[1]
values = list(map(float, values.split()))


# EssenceList[0].price = 1
# EssenceList[1].price = 1
# EssenceList[2].price = 1
# EssenceList[3].price = 1
# EssenceList[4].price = 1
# EssenceList[5].price = 1
# EssenceList[6].price = 1
# EssenceList[7].price = 1
# EssenceList[8].price = 1
# EssenceList[9].price = 1
# EssenceList[10].price = 1
# EssenceList[11].price = 1
# EssenceList[12].price = 1
# EssenceList[13].price = 1
# EssenceList[14].price = 1
# EssenceList[15].price = 1
# EssenceList[16].price = 1
# EssenceList[17].price = 1
# EssenceList[18].price = 1
# EssenceList[19].price = 1
# EssenceList[20].price = 1
# EssenceList[21].price = 1
# EssenceList[22].price = 1
# EssenceList[23].price = 1



def SetPriceFirstHalf(args):
    
    pyautogui.moveTo(args[0])
    pyautogui.rightClick(args[0])
    pyautogui.moveTo([args[0][0], args[0][1]+100])
    pyautogui.click([args[0][0] , args[0][1]+100])
    pyautogui.moveTo([args[0][0] , args[0][1]+220])
    pyautogui.click([args[0][0] , args[0][1]+220])
    pyautogui.moveTo([args[0][0] + 200, args[0][1] +100])
    pyautogui.click([args[0][0] + 200, args[0][1] + 100])
    pyautogui.press("backspace")
    pyautogui.press("backspace")
    pyautogui.press("backspace")
    pyautogui.write(str(args[1]))
    pyautogui.moveTo([args[0][0] + 540, args[0][1] + 170])
    pyautogui.click([args[0][0] + 540, args[0][1] + 170])



def SetPriceSecondHalf(args):
    
    pyautogui.moveTo(args[0])
    pyautogui.rightClick(args[0])
    pyautogui.moveTo([args[0][0] - 190, args[0][1] + 110])
    pyautogui.click([args[0][0] - 190 , args[0][1] + 110])
    pyautogui.moveTo([args[0][0] - 240 , args[0][1] + 215])
    pyautogui.click([args[0][0] - 240 , args[0][1] + 215])
    pyautogui.moveTo([args[0][0] - 30, args[0][1] + 110])
    pyautogui.click([args[0][0] - 30, args[0][1] + 110])
    pyautogui.press("backspace")
    pyautogui.press("backspace")
    pyautogui.press("backspace")
    pyautogui.write(str(args[1]))
    pyautogui.moveTo([args[0][0] + 300, args[0][1] + 170])
    pyautogui.click([args[0][0] + 300, args[0][1] + 170])
    
    

image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
image = image[0:1440, 0:2560]


Clickthis = ()
print("start")


for i in range (len(EssenceList)):
    if values[i] == 0:
        continue   
    sub = 33
    cord = EssenceList[i].StashLocation
    img = image[cord[1]-sub:cord[1]+sub, cord[0]-sub:cord[0]+sub]
    if np.average(img) < 30:
        continue
   
    Clickthis = (EssenceList[i].StashLocation,int(  math.ceil(EssenceList[i].price + 1)))
    if (i<12):
        SetPriceFirstHalf(Clickthis)
    else:
        SetPriceSecondHalf(Clickthis)
        
print("finish")                
