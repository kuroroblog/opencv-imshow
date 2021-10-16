import cv2
import sys

# imread : 画像ファイルを読み込んで、多次元配列(numpy.ndarray)にする。
# imreadについて : https://kuroro.blog/python/wqh9VIEmRXS4ZAA7C4wd/
# 第一引数 : 画像のファイルパス
# 戻り値 : 行 x 列 x 色の三次元配列(numpy.ndarray)が返される。
img = cv2.imread('./input.jpg')

# 画像ファイルが正常に読み込めなかった場合、プログラムを終了する。
if img is None:
    sys.exit("Could not read the image.")

# imshow : ウィンドウへ画像を表示する関数
# 第一引数 : ウィンドウ名(自由に命名ください)
# 第二引数 : 多次元配列(画像情報)
# <第二引数の例>
# [
# [
# [234 237 228]
# ...
# [202 209 194]
# ]
# [
# [10 27 16]
# ...
# [36 67 46]
# ]
# [
# [34 51 40]
# ...
# [50 81 60]
# ]
# ]
# imshowに関する公式ドキュメント : https://docs.opencv.org/master/d7/dfc/group__highgui.html#ga453d42fe4cb60e5723281a89973ee563
cv2.imshow('image', img)

# waitkey : 画像を表示するウィンドウからの、キーボード入力を待ち受ける関数
# waitkeyについて : https://kuroro.blog/python/8DIolh7Pwggq2pvabysn/

# 第一引数 : 画像を表示するウィンドウからの、キーボード入力を待ち受ける時間。ミリ秒単位指定。int型。
# (例) 1000を指定すると、1秒間キーボード入力を待ち受ける。2000を指定すると、2秒間キーボード入力を待ち受ける。
# ミリ秒とは? : https://e-words.jp/w/%E3%83%9F%E3%83%AA%E7%A7%92.html#:~:text=%E3%83%9F%E3%83%AA%E7%A7%92%E3%81%A8%E3%81%AF%E3%80%81%E6%99%82%E9%96%93,1%E7%A7%92%E3%81%AB%E7%9B%B8%E5%BD%93%E3%81%99%E3%82%8B%E3%80%82
# ※ 0以下の数字を指定すると、画像を表示するウィンドウからの、キーボード入力が発生しない限り、ウィンドウを表示し続けます。

# 戻り値 : キーボード入力した文字を、10進数で表記するアスキーコードの値で返す。
# 10進数とは? : https://wa3.i-3-i.info/word1608.html
# アスキーコードとは? : https://wa3.i-3-i.info/word15290.html
# アスキーコード表 : https://www.k-cube.co.jp/wakaba/server/ascii_code.html
k = cv2.waitKey(0)

# キーボードから's'の文字が入力された場合、画像を保存する。
# ord : 文字をアスキーコードの値へ変換する。
if k == ord('s'):
    # imwrite : 画像の保存を行う関数
    # 第一引数 : 保存先の画像ファイル名
    # 第二引数 : 多次元配列(numpy.ndarray)
    # <第二引数の例>
    # [
    # [
    # [234 237 228]
    # ...
    # [202 209 194]
    # ]
    # [
    # [10 27 16]
    # ...
    # [36 67 46]
    # ]
    # [
    # [34 51 40]
    # ...
    # [50 81 60]
    # ]
    # ]
    # imwriteについて : https://kuroro.blog/python/i0tNE1Mp8aEz8Z7n6Ggg/
    cv2.imwrite('output.jpg', img)

# destroyAllWindows : 全てのウィンドウを閉じる関数
# destroyAllWindowsに関する公式ドキュメント : https://docs.opencv.org/master/d7/dfc/group__highgui.html#ga6b7fc1c1a8960438156912027b38f481
# もしくは、cv2.destroyAllWindow('image')。imageはウィンドウ名。
# destroyAllWindow : 指定するウィンドウ名に紐づく、ウィンドウを閉じる関数
# destroyAllWindowに関する公式ドキュメント : https://docs.opencv.org/master/d7/dfc/group__highgui.html#ga851ccdd6961022d1d5b4c4f255dbab34
cv2.destroyAllWindows()
