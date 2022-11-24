import requests as req
import numpy as np
import cv2
import cv2u
import tkinter
from icrawler.builtin import BingImageCrawler as BIC
import pathlib as plib
import time

def pil2cv(image):
    ''' PIL型 -> OpenCV型 '''
    new_image = np.array(image, dtype=np.uint8)
    if new_image.ndim == 2:  # モノクロ
        print('モノクロ')
        pass
    elif new_image.shape[2] == 3:  # カラー
        print('カラー')
        new_image = cv2.cvtColor(new_image, cv2.COLOR_RGB2BGR)
    elif new_image.shape[2] == 4:  # 透過
        print('透過')
        new_image = cv2.cvtColor(new_image, cv2.COLOR_RGBA2BGRA)
    return new_image


def show_img():

    output_dir = './' + name.get()
    # GUIテキストボックスからキーワード・保存する数・保存フォルダ名を入力して保存
    bing_crawler = BIC(downloader_threads=4,storage={"root_dir" : name.get()})
    bing_crawler.crawl(keyword=keyword.get(), filters=None, offset=0, max_num=int(amount.get()))

    all_image = list(plib.Path(name.get()).glob("**/*.jpg"))
    img_list = []

    for i in range(1, len(all_image) - 1):
        img = cv2.imread(str(all_image[i - 1]), cv2.IMREAD_GRAYSCALE)
        img_resize = cv2.resize(img, (100, 100))
        output_path = output_dir + '/' + all_image[i - 1].name
        cv2.imwrite(output_path, img_resize)
        img_resize = pil2cv(img_resize)
        img_list.append(output_path)
        margeimg = cv2.vconcat(img_list[i - 2], img_list[i - 1])
    
    
    cv2.imwrite("./margeimg.jpg", margeimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



#urlbox描画
root = tkinter.Tk()
root.geometry("300x200")
root.title("画像一括保存")
label1 = tkinter.Label(text = "検索ワード")
label1.place(x = 30, y = 70)

label2 = tkinter.Label(text = "保存する数")
label2.place(x = 30, y = 100)

label3 = tkinter.Label(text = "フォルダ名")
label3.place(x = 30, y = 130)

keyword = tkinter.Entry(width = 20)
keyword.place(x = 90, y = 70)
amount = tkinter.Entry(width = 20)
amount.place(x = 90, y = 100)
name = tkinter.Entry(width = 20)
name.place(x = 90, y = 130)




btn = tkinter.Button(root, text = "Go", command=show_img)
btn.place(x = 140, y = 170)

root.mainloop()