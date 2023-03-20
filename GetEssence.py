import pyautogui
import sys
import time
from pynput.mouse import Button, Controller

mouse = Controller()


# pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.1


class Essence:
    def __init__(self, name, base, StashLocation):
        self.name = name
        self.base = base
        self.StashLocation = StashLocation

EssenceList = [ Essence("DeafeningEssenceofGreed", 9, [80,244]),
         Essence("DeafeningEssenceofContempt",9, [80,300]), Essence("DeafeningEssenceofHatred", 9, [80,365]), Essence ("DeafeningEssenceofWoe", 9, [80,434]), Essence("DeafeningEssenceofFear", 20, [80,508]),
Essence("DeafeningEssenceofAnger",  9,[80,570]), Essence("DeafeningEssenceofTorment", 9, [80,635]), Essence("DeafeningEssenceofSorrow", 9, [80,690]), Essence("DeafeningEssenceofRage", 9,[80,760]),
Essence("DeafeningEssenceofSuffering", 9, [80,830]), Essence("DeafeningEssenceofWrath",9,[80,900]), Essence("DeafeningEssenceofDoubt", 9,[80,960]), Essence("DeafeningEssenceofLoathing", 9, [790,240]),
Essence("DeafeningEssenceofZeal",9,[790,300]), Essence("DeafeningEssenceofAnguish", 9,[790,365]), Essence("DeafeningEssenceofSpite", 9, [790,435]), Essence("DeafeningEssenceofScorn", 9, [790,500]), 
Essence("DeafeningEssenceofEnvy", 9, [790,570]),Essence("DeafeningEssenceofMisery", 9, [790,633]),Essence("DeafeningEssenceofDread", 9, [790,690]),Essence("EssenceofInsanity", 9, [790,765]),
Essence("EssenceofHorror", 9, [790,830]),Essence("EssenceofDelirium", 9, [790,890]),Essence("EssenceofHysteria", 9, [790,960]),]

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


    


