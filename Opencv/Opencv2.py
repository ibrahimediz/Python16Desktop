import cv2 # opencv
import numpy as np # matris işlemleri için
from matplotlib import pyplot as plt # ekranda göstermek için

img = cv2.imread(r'Opencv\resimler\bookpage.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# retval,treshold = cv2.threshold(gray,10,255,cv2.THRESH_BINARY)
th = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow('resim',img)
cv2.imshow('eşik',th)
cv2.waitKey(0)
cv2.destroyAllWindows()