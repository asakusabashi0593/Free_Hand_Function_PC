import pyautogui
import time
# print(pyautogui.size())
searchposition = [545, 1060]
To_Yahoo_position = [280, 530]
input_URL_position = [390, 65]
To_My_Github_position = [320, 410]
My_Github_URL = "https"+ str(":") + "//github.com/asakusabashi0593"
# print(pyautogui.position())
def To_MY_URL(searchposition, To_Yahoo_position ,input_URL_position, To_My_Github_position, My_Github_URL): 
    pyautogui.moveTo(searchposition[0], searchposition[1] ,duration=1)
    pyautogui.click()
    pyautogui.write("Yahoo! Japan", interval=0.4)
    pyautogui.press("enter")
    pyautogui.moveTo(To_Yahoo_position[0], To_Yahoo_position[1] ,duration=1.5)
    pyautogui.click()
    pyautogui.moveTo(input_URL_position[0], input_URL_position[1] ,duration=1.5)
    pyautogui.click()
    pyautogui.hotkey("ctrl", "a", "backspace")

    
    pyautogui.write(My_Github_URL, interval=0.15)
    pyautogui.press("enter")

    pyautogui.moveTo(To_My_Github_position[0], To_My_Github_position[1] ,duration=1)
    pyautogui.click()
    return 0




if __name__ == "__main__":
    time.sleep(3)
    To_MY_URL(searchposition, To_Yahoo_position ,input_URL_position, To_My_Github_position, My_Github_URL)