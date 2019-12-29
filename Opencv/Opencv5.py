import cv2 # opencv
import numpy as np # matris işlemleri için
from matplotlib import pyplot as plt # ekranda göstermek için


cap = cv2.VideoCapture(0)
facecas = cv2.CascadeClassifier(r"Opencv\cascades\haarcascade_frontalface_default.xml")
eyecas = cv2.CascadeClassifier(r"Opencv\cascades\haarcascade_eye.xml")

while 1:
    _,img = cap.read()
    
    # fgmask = fgbg.apply(img)

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    yuzler = facecas.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in yuzler:
        # px = img[y:y+h,x:x+w]
        # kernel = np.ones((15,15),np.float32)/225
        # smoothed = cv2.filter2D(px,-1,kernel)
        # blur = cv2.GaussianBlur(px,(15,15),2)
        # img[y:y+h,x:x+w] = blur
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_g = gray[y:y+h,x:x+w]
        roi_img = img[y:y+h,x:x+w]
        gozler = eyecas.detectMultiScale(roi_g)
        for (ex,ey,ew,eh) in gozler:
            cv2.rectangle(roi_img,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)

   
    cv2.imshow('resim',img)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()