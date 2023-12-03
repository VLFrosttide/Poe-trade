import pyautogui
import sys
import time
from pynput.mouse import Button, Controller
from Essence import *

mouse = Controller()


# pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.1


RequestEssenceQuant = int(sys.argv[1])
RequestTypeEssence = None
for i in EssenceList:
    if i.name == sys.argv[2]:
        RequestTypeEssence=i
        break
     

kolko = int(RequestEssenceQuant/RequestTypeEssence.base)
print(kolko)
sys.stdout.flush()
remain = RequestEssenceQuant%RequestTypeEssence.base 
def Get_Essence():
    pyautogui.keyDown("ctrl")   
    pyautogui.moveTo(x=RequestTypeEssence.StashLocation[0],y=RequestTypeEssence.StashLocation[1])
    pyautogui.click(x=RequestTypeEssence.StashLocation[0],y=RequestTypeEssence.StashLocation[1])
    pyautogui.keyUp("ctrl")

def Get_Remaining(remain):
    pyautogui.keyDown("shift")   
    pyautogui.click(x=RequestTypeEssence.StashLocation[0],y=RequestTypeEssence.StashLocation[1])
    pyautogui.keyUp("shift")
    for i in str(remain):
        pyautogui.press(i, interval=0.1)

    pyautogui.press("enter")
    pyautogui.moveTo(x=2505, y=1100)

    pyautogui.click(x=2505, y=1100)

if RequestEssenceQuant<=RequestTypeEssence.base:
    print("remain")
    sys.stdout.flush()
    pyautogui.keyDown("shift")   
    pyautogui.moveTo(x=RequestTypeEssence.StashLocation[0],y=RequestTypeEssence.StashLocation[1])
    pyautogui.click(x=RequestTypeEssence.StashLocation[0],y=RequestTypeEssence.StashLocation[1])
    pyautogui.keyUp("shift")
    
    time.sleep(0.2)
    for i in str (RequestEssenceQuant):
        pyautogui.press(i, interval=0.1)
    time.sleep(0.2)
    # pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.moveTo(x=2505, y=1100)
    pyautogui.click(x=2505, y=1100)



if RequestEssenceQuant>RequestTypeEssence.base:
    for i in range(0,kolko):
        Get_Essence()
      
        
if remain != 0 and RequestEssenceQuant>RequestTypeEssence.base:
    #time.sleep(1)
    Get_Remaining(remain)
    print("remain")
    sys.stdout.flush()


    


