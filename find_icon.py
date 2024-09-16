import pyautogui
import time

def find_location_img(png):


    # 再度 'win' + 'd' でウィンドウを元に戻す
    try:
        time.sleep(3)
        # 全てのウィンドウを最小化する (Windows)
        pyautogui.hotkey('win', 'd')  # 'win' + 'd' はデスクトップを表示し、全てのウィンドウを最小化します

        # 少し待機してスクリーンショットを撮る
        time.sleep(1)  # 1秒待機してからスクリーンショットを撮る
        # スクリーンショットを取得 (現在は使用されていないため、コメント化可能)
        # screen_shot = pyautogui.screenshot()
        # スクリーンショットから特定の画像の位置を検索
        location = pyautogui.locateOnScreen(png + ".png", confidence=0.8)
        if location:
            # 画像の位置が見つかった場合、その座標を取得
            center = pyautogui.center(location)
            return center
        else:
            # 画像が見つからなかった場合
            return (-1, -1)
    except pyautogui.ImageNotFoundException:
        # 例外処理: 画像が見つからなかった場合
        print(f"Image '{png}.png' not found on the screen.")
        return (-1, -1)
    except Exception as e:
        # 予期しないエラーが発生した場合
        print(f"An error occurred: {e}")
        return (-1, -1)
    
if __name__ == "__main__":
    png = "Chrome"
    # print(find_location_img(png))
    x, y = find_location_img(png)
    pyautogui.moveTo(x, y ,duration=1)
    # print( png + ".png")
    # print(pyautogui.__version__)