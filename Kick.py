import pyautogui
import sys
import time
PlayerName = sys.argv[1]
pyautogui.press("enter")
time.sleep(0.5)
pyautogui.write(f"/kick {PlayerName}")
time.sleep(0.5)
pyautogui.press("enter")
print(sys.argv[1])
sys.stdout.flush()