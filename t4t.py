import sys  
import pyautogui
import time


PlayerName = sys.argv[1]
# PlayerName = "Baahmaaamu"
pyautogui.click(150,150)
pyautogui.press("enter")
time.sleep(1)
pyautogui.write(f"@{PlayerName} t4t")
time.sleep(1)
pyautogui.press("enter")