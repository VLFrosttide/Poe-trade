
import utils
import cv2
import pyautogui
from pynput.keyboard import Key, Listener
import numpy as np
import matplotlib.pylab as plt
from multiprocessing import Pool
import sys


def get_col_info(image, start_x, start_y, add, col, assets):
    count = {}
    for row in range(5):
        vertical = [start_y+add*row, start_y+add*(row+1)]
        horizontal = [start_x+add*col, start_x+add*(col+1)]

        cell_img = image[vertical[0]:vertical[1], horizontal[0]:horizontal[1]]

        sim_img = utils.comparable(cell_img)
        sim = utils.similar(sim_img, assets)
        if sim == None:
            continue
        txt_img = cell_img[0:27, 0:40]
        sim_str = sim[0]


        txt = utils.get_text(txt_img)
        
        txt_int = int(txt) if txt.isnumeric() else 1
        count[sim_str] = count[sim_str] + txt_int if sim_str in count else txt_int

    return count

def save_inventory_png(start_x, start_y, add, image):
    plt.figure(figsize=(15, 15))
    count = 1
    for j in range(12):
        for i in range(5):
            v = [start_y+add*i, start_y+add*(i+1)]
            h = [start_x+add*j, start_x+add*(j+1)]
            img = image[v[0]:v[1], h[0]:h[1]]
            ax = plt.subplot(10, 12, count)
            plt.imshow(img)
            plt.axis("off")
            plt.tight_layout()
            count += 1
    plt.savefig("debug.png")
    
    

def scan_inventory(start_x, start_y, add, required, assets , debug=False):
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    image = image[0:1440, 0:2560]
    final_count = {}

    pool = Pool()
    processes = []
    for j in range(12):
        process = pool.apply_async(get_col_info, [image, start_x, start_y, add, j, assets])
        processes.append(process)

    for process in processes:
        result = process.get()
        for item, count in result.items():
            final_count[item] = final_count[item] + count if item in final_count else count

    if debug:
        print("DEBUG ON: Saving image 'debug.png'")
        save_inventory_png(start_x, start_y, add, image)
        print("Values Read from image: ")
        for item, count in final_count.items():
            print(f"'{item}': {count}")

    
    intersection = dict(final_count.items() & required.items())
    if len(intersection) == len(required):
        return True
    else:
        return False
if __name__ == "__main__":
    
    assets = utils.Init_imgs("Currency")     
    start_x = 416
    start_y = 273
    Quant = int(sys.argv[1])
    Name = sys.argv[2]
    # Quant = 55
    # Name = "ChaosOrb"

    result = scan_inventory(start_x,start_y,70,{Name:Quant},assets, True)
    print(result)
    sys.stdout.flush()

