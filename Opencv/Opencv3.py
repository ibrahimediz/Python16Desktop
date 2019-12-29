import cv2 # opencv
import numpy as np # matris işlemleri için
from matplotlib import pyplot as plt # ekranda göstermek için

img = cv2.imread(r'Opencv\resimler\res1.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# retval,th = cv2.threshold(gray,100,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# th = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

low = np.array([30,150,50])
upp = np.array([255,255,180])

mask = cv2.inRange(hsv,low,upp)
res = cv2.bitwise_and(img,img,mask=mask)



cv2.imshow('resim',img)
cv2.imshow('maske',mask)
cv2.imshow('sonuc',res) 

cv2.waitKey(0)
cv2.destroyAllWindows()