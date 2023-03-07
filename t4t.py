import sys  
import pyautogui

PlayerName = sys.argv[1]

pyautogui.press("enter")
pyautogui.write(f"@{PlayerName} t4t")
pyautogui.press("enter")