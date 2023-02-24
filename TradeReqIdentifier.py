import pyautogui


while 1:
    if pyautogui.locateOnScreen("TradeRequest.png") !=None:
        print("Found")
    else:
        print("NotThere")