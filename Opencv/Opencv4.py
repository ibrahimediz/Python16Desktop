import cv2 # opencv
import numpy as np # matris işlemleri için
from matplotlib import pyplot as plt # ekranda göstermek için


cap = cv2.VideoCapture(0)

while 1:
    _,img = cap.read()

# img = cv2.imread(r'Opencv\resimler\res1.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# retval,th = cv2.threshold(gray,100,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# th = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
    # hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # low = np.array([30,150,50])
    # upp = np.array([255,255,180])
    # mask = cv2.inRange(hsv,low,upp)
    # res = cv2.bitwise_and(img,img,mask=mask)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    temp = cv2.imread(r'Opencv\resimler\template.png',0)
    w,h = temp.shape[::-1]
    res = cv2.matchTemplate(gray,temp,cv2.TM_CCOEFF_NORMED)
    th = 2
    loc = np.where(res >= th)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)
    cv2.imshow('tespit',img)
    # cv2.imshow('resim',img)
    # cv2.imshow('maske',mask)
    # cv2.imshow('sonuc',res) 
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()