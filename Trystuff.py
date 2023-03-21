import pyautogui


pyautogui.moveTo(args[0])
pyautogui.rightClick(args[0])
pyautogui.moveTo(args[0] + 100pxY)
pyautogui.click(args[0] + 100pxY)
pyautogui.moveTo(args[0] + 220pxY)
pyautogui.click(args[0] + 220pxY)
pyautogui.moveTo(args[0] + 100pxY and +200pxX)
pyautogui.click(args[0] + 100pxY and +200pxX)
pyautogui.write(args[1])
pyautogui.moveTo(args[0] + 170pxY and +540pxX)