import cv2 # opencv
import numpy as np # matris işlemleri için
from matplotlib import pyplot as plt # ekranda göstermek için

img = cv2.imread(r'Opencv\resimler\pink-lotus-3021709_1280.jpg')

px = img[600:700,700:900]
print(px)
img[300:400,600:800] = px
print(img.shape)
print(img.size)
print(img.dtype)
cv2.imshow('resim',img)
cv2.waitKey(0)
cv2.destroyAllWindows()