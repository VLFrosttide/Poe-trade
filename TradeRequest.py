import pyautogui
import sys
import time
PlayerName = sys.argv[1]
pyautogui.press("enter")
time.sleep(0.2)
pyautogui.write(f"/tradewith {PlayerName}")
time.sleep(0.2)
pyautogui.press("enter")