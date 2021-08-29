import cv2
import sys

# imread : 画像ファイルを読み込んで、多次元配列(numpy.ndarray)にする。
# imreadについて : https://kuroro.blog/python/wqh9VIEmRXS4ZAA7C4wd/
# 第一引数 : 画像のファイルパス
# 戻り値 : 行(高さ) x 列(幅) x 色の三次元配列(numpy.ndarray)が返される。
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

# waitKey : ウィンドウを表示し続ける時間を設定する関数。
# Pythonプログラムの終了とともに、ウィンドウがすぐに閉じられてしまうため、waitKey関数を利用する。
##########################################################
# 第一引数 : ウィンドウを表示し続ける時間。ミリ秒単位で指定する。(例)1000を指定すると、1秒間ウィンドウを表示し続ける。2000を指定すると、2秒間ウィンドウを表示し続ける。
# ミリ秒とは? : https://e-words.jp/w/%E3%83%9F%E3%83%AA%E7%A7%92.html#:~:text=%E3%83%9F%E3%83%AA%E7%A7%92%E3%81%A8%E3%81%AF%E3%80%81%E6%99%82%E9%96%93,1%E7%A7%92%E3%81%AB%E7%9B%B8%E5%BD%93%E3%81%99%E3%82%8B%E3%80%82
# 0を指定する場合、0秒間ウィンドウを表示し続けるという意味ではなく、キーボードのどれかの文字が押されるまで、継続的にウィンドウを表示し続けるという意味になる。
##########################################################
# 戻り値 : 第一引数へ0以外を指定する場合、-1が返される。第一引数へ0を指定する場合、ASCIIコード表の番号が返される。
# ASCIIコードとは? : http://www3.nit.ac.jp/~tamura/ex2/ascii.html
# waitKeyに関する公式ドキュメント : https://docs.opencv.org/master/d7/dfc/group__highgui.html#ga5628525ad33f52eab17feebcfba38bd7
k = cv2.waitKey(0)

# キーボードからsの文字が入力された場合、画像を保存する。
# ord : 文字をASCIIコードへ変換する。
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
