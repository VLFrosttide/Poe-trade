import pyautogui
import sys
import time
from pynput.mouse import Button, Controller
from Currency import *

mouse = Controller()


# pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.1

RequestCurrencyQuant = int(sys.argv[1])
# RequestCurrencyQuant = 1
RequestTypeCurrency = None
for i in CurrencyList:
    if i.name == sys.argv[2]:
        RequestTypeCurrency=i
        break
     

kolko = int(RequestCurrencyQuant/RequestTypeCurrency.base)
print(f"Clicks {kolko}")
remain = RequestCurrencyQuant%RequestTypeCurrency.base 
def Get_Currency():
    pyautogui.keyDown("ctrl")   
    pyautogui.moveTo(x=RequestTypeCurrency.StashLocation[0],y=RequestTypeCurrency.StashLocation[1])
    pyautogui.click(x=RequestTypeCurrency.StashLocation[0],y=RequestTypeCurrency.StashLocation[1])
    pyautogui.keyUp("ctrl")

def Get_Remaining(remain):
    pyautogui.keyDown("shift")   
    pyautogui.click(x=RequestTypeCurrency.StashLocation[0],y=RequestTypeCurrency.StashLocation[1])
    pyautogui.keyUp("shift")
    for i in str(remain):
        pyautogui.press(i, interval=0.1)

    pyautogui.press("enter")
    pyautogui.moveTo(x=2505, y=1100)

    pyautogui.click(x=2505, y=1100)

if RequestCurrencyQuant<=RequestTypeCurrency.base:
    print("remain", flush=True)
    pyautogui.keyDown("shift")   
    pyautogui.moveTo(x=RequestTypeCurrency.StashLocation[0],y=RequestTypeCurrency.StashLocation[1]
                     
                     )
    pyautogui.click(x=RequestTypeCurrency.StashLocation[0],y=RequestTypeCurrency.StashLocation[1])
    pyautogui.keyUp("shift")
    
    time.sleep(0.2)
    for i in str (RequestCurrencyQuant):
        pyautogui.press(i, interval=0.1)
    time.sleep(0.2)
    # pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.moveTo(x=2505, y=1100)
    pyautogui.click(x=2505, y=1100)



if RequestCurrencyQuant>RequestTypeCurrency.base:
    for i in range(0,kolko):
        Get_Currency()
      
        
if remain != 0 and RequestCurrencyQuant>RequestTypeCurrency.base:
    #time.sleep(1)
    Get_Remaining(remain)
    print("remain",flush=True)


    


