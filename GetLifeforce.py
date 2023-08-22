import pyautogui
import sys
import time

Quant = sys.argv[1]
LifeforceName =  sys.argv[2]

if LifeforceName == "WildCrystallisedLifeforce" :
    print("wildworks11111")
    pyautogui.moveTo(180,720)
    pyautogui.keyDown("shift")
    pyautogui.click(180,720)
    pyautogui.keyUp("shift")
    time.sleep(0.3)
    pyautogui.write(str(Quant))
    time.sleep(0.3)
    pyautogui.press("enter")
    time.sleep(0.2)
    pyautogui.moveTo(2500,1100)
    pyautogui.click(2500,1100)
    
if LifeforceName == "VividCrystallisedLifeforce" :
    print("vividworks2222222222")
    pyautogui.moveTo(260,720)
    pyautogui.keyDown("shift")
    pyautogui.click(260,720)
    pyautogui.keyUp("shift")
    time.sleep(0.3)
    pyautogui.write(str(Quant))
    time.sleep(0.3)
    pyautogui.press("enter")
    time.sleep(0.2)
    pyautogui.moveTo(2500,1100)
    pyautogui.click(2500,1100)
    
if LifeforceName == "PrimalCrystallisedLifeforce" :
    print("Primalworks3333333")
    pyautogui.moveTo(620,720)
    pyautogui.keyDown("shift")
    pyautogui.click(620,720)
    pyautogui.keyUp("shift")
    time.sleep(0.3)
    pyautogui.write(str(Quant))
    time.sleep(0.3)
    pyautogui.press("enter")
    time.sleep(0.2)
    pyautogui.moveTo(2500,1100)
    pyautogui.click(2500,1100)