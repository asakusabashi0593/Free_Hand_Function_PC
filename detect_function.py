import cv2
import numpy as np
import pyautogui
import find_icon
import Move
import time
import find_character
import screenshot
def init():
    # カメラキャプチャの初期化と顔認識用カスケードの読み込み
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    return cap, face_cascade

def detect_face(cap, face_cascade):

    ret, frame = cap.read()
    if not ret:
        return False, None
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)  # 青色の矩形で顔を囲む
    return (len(faces) > 0), frame

def activate_function():
    # Move to Chrome brouser
    x, y = find_icon.find_location_img("Firefox")
    print(x,y)
    Move.move(x , y, 2)
    screen = screenshot.get_screen()
    # x, y = find_character.find_text(screen, 'Googleで検索')
    print(find_character.find_text(screen, 'Googleで検索'))
    Move.move(x , y, 1)
    my_url = "https"+ str(":") + "//github.com/asakusabashi0593" 
    pyautogui.write(my_url, interval=0.7)
    print("顔が100フレーム連続で検出されました！機能を起動します。")

def main():
    cap, face_cascade = init()
    frame_counter = 0
    while True:
        detected, frame = detect_face(cap, face_cascade)
        if detected:
            frame_counter += 1
            if frame_counter >= 1:
                flag = True
                frame_counter = 0  # 機能起動後、カウンターをリセット
        else:
            frame_counter = 0  # 顔が検出されなければカウンターをリセット
            flag = False
        cv2.imshow('Face Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q') or flag:
            break
    if flag:
        cap.release()
        cv2.destroyAllWindows()
        activate_function()
    else:
        cap.release()
        cv2.destroyAllWindows()      

if __name__ == "__main__":
    main()