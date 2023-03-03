import pyautogui
import sys
import time

t_end = time.time() + 300

while time.time() < t_end:
    if pyautogui.locateOnScreen("Trade.png"):
        print("Found")
        sys.stdout.flush()
        break


