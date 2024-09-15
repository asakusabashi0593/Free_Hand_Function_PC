#pip install easyocr
#pip install opencv-python

import cv2
import easyocr
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning) # FutureWarningを非表示にする
reader = easyocr.Reader(['ja','en'], verbose=False) # この処理は時間がかかる





def find_text(img, target_text):
    '''画像内からターゲットの文字列を読み取ってその中心座標を返す関数
    Args:
        img (image): 文字を読み取りたい画像
        target_text (str): ターゲットのテキスト
    Returns:
        pos (list): ターゲットテキストの中心座標(x,y)
    '''
    
    results = reader.readtext(img)
    pos = (-1, -1)

    for result in results:
        if target_text in result[1]:
            # バウンディングボックスの座標を取得
            bbox = result[0]
            
            # 座標を変数に代入
            x1, y1 = bbox[0]
            x2, y2 = bbox[1]
            x3, y3 = bbox[2]
            x4, y4 = bbox[3]

            # 中心座標を計算
            center_x = (x1 + x2 + x3 + x4) / 4
            center_y = (y1 + y2 + y3 + y4) / 4
            pos = (int(center_x), int(center_y))

            break
    
    if pos == (-1, -1):
        print('target_text not found.')
    
    return pos





def read_texts(img):
    '''画像内の文字列を読み取って文字列を返す関数
    Args:
        img (image): 文字を読み取りたい画像
    Returns:
        texts (list): 読み取った文字列が収納された配列
    '''
    
    texts = reader.readtext(img, detail=0)
    
    return texts





def is_text_in_image(img, target_text):
    '''画像内のなかにターゲットのテキストが存在するか確認する関数
    Args:
        img (image): 文字を読み取りたい画像
        target_text (str): ターゲットのテキスト
    Returns:
        isTextInImage (bool): 画像内のなかにターゲットのテキストが存在するか否か
    '''

    texts = reader.readtext(img, detail=0)
    extracted_text = ''.join([text for text in texts])
    isTextInImage = target_text in extracted_text

    return isTextInImage





if __name__ == "__main__":
    ## for debugging
    img = cv2.imread("C:/Users/User/Pictures/Screenshots/aaa.png")
    target = '検索または'

    pos = find_text(img, target)
    print(pos)
    texts = read_texts(img)
    print(texts)
    flag = is_text_in_image(img, target)
    print(flag)
    