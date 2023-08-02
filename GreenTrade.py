import pyautogui
import sys
import time

t_end = time.time() + 300
while time.time() < t_end:
    pix = pyautogui.pixel(1255,605)
    val = pix[1]
    if val == 44:
        print("Accepted")
        sys.stdout.flush()
        # break
    else:
        print(val)
    # time.sleep(1)  