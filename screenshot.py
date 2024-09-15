import cv2
import pyautogui
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy



def show(img):
    '''画像の表示
    Args:
        img (image): 描画したい画像
    '''
    plt.imshow(img, vmin=0, vmax=255)
    plt.show()





def get_screen(region=None):
    '''プレイエリアキャプチャ
    Args:
        region (taple): スクショしたい領域(x, y, +x, +y)
    Returns:
        img (image): cv2系の画像データ
    '''
    img = pyautogui.screenshot(region=region) #PIL系でキャプチャされる
    return np.array(img, 'uint8') #cv2系で返す