import pyautogui
import sys
import time
name = str(sys.argv[1])
pyautogui.press("enter")
time.sleep(0.2)

pyautogui.write(f"/invite { name}")
time.sleep(0.2)
pyautogui.press("enter")                                   