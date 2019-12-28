import cv2 # opencv
import numpy as np # matris işlemleri için
from matplotlib import pyplot as plt # ekranda göstermek için

img = cv2.imread(r'Opencv\resimler\res1.jpg')
# img[0:40] = 255
# print(img[0:20])
cv2.line(img,(10,10),(60,60),(255,255,255),3)
cv2.rectangle(img,(10,10),(60,60),(255,255,255),1,cv2.LINE_AA)
cv2.circle(img,(30,30),30,(255,255,255),1)
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,"Merhaba",(0,80),font,2,(255,255,255),1,cv2.LINE_AA)

cv2.imshow('resim',img)
cv2.waitKey(0)
cv2.destroyAllWindows()