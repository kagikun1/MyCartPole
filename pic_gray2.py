from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import ThreadPool
from threading import Thread
import numpy as np
import cv2
import pathlib as plib
import time
import os

# def show_img():
#     for i in range(0, len(all_image)):
#         img = cv2.imread(str(all_image[i]), cv2.IMREAD_GRAYSCALE)
#         output_path = output_dir + '/' + all_image[i].name
#         cv2.imwrite(output_path, img)

def show_img1():
    for i in range(0, len(all_image) // 2):
        img = cv2.imread(str(all_image[i]), cv2.IMREAD_GRAYSCALE)
        output_path = output_dir + '/' + all_image[i].name
        cv2.imwrite(output_path, img)

def show_img2():
    for i in range(len(all_image) // 2 + 1, len(all_image), 1):
        img = cv2.imread(str(all_image[i]), cv2.IMREAD_GRAYSCALE)
        output_path = output_dir + '/' + all_image[i].name
        cv2.imwrite(output_path, img)
        
if __name__ == "__main__":
    t1 = time.perf_counter()
    input_dir = './FullColor'
    output_dir = './gray'
    all_image = list(plib.Path(input_dir).glob("**/*.jpg"))

    # show_img()
    with ThreadPoolExecutor(max_workers=os.cpu_count()) as ex:
        ex.submit(show_img1())
        ex.submit(show_img2())
    
    t2 = time.perf_counter()
    end = t2 - t1

    print(f'処理時間 ： {end}')

    