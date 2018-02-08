# -*- coding: utf-8 -*-
import cv2
from PIL import Image
import numpy as np
# 画像の読み込み
img = Image.open("rgreen.png")
img = cv2.imread(img, 1)

# 画像の高さ、幅を取得
height = int(img.shape[0]/2)
width = int(img.shape[1]/2)
# 中央右寄りに、青で塗りつぶされた円形を描く
img = cv2.circle(img, (width, height), 40, (255, 255, 255), -1)

img2 = Image.new('RGB', (width*2, height*2))
img_pixels = np.array([[img.getpixel((i,j)) for j in range(height)] for i in range(width)])
img_pixels.show()
