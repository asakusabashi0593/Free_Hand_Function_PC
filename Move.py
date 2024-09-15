import pyautogui
import time

def move(x,y, num):
    # movint to particular coordinate
    pyautogui.moveTo(x, y ,duration=1)
    # this part conduct click num times
    pyautogui.click()
    pyautogui.click()
    return 