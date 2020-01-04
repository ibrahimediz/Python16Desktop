import cv2
import numpy as np
from PIL import Image
import os,json


tani = cv2.face.LBPHFaceRecognizer_create()
tani.read('trainer.yml')
detector = cv2.CascadeClassifier("Opencv\cascades\haarcascade_frontalface_default.xml")

font = cv2.FONT_HERSHEY_COMPLEX
id = 0

dictionary = {}
name = []
dosya = open('ids.json')
dictionary = json.load(dosya)
cam = cv2.VideoCapture(0)

for key,values in dictionary.items():
    name.append(key)

while True:
    ret,cerceve = cam.read()
    cerceve = cv2.flip(cerceve,1)
    gri = cv2.cvtColor(cerceve,cv2.COLOR_BGR2GRAY)
    id = "bilinmiyor"
    faces = detector.detectMultiScale(gri,1.7,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(cerceve,(x,y),(x+w,y+h),(0,255,0),2)
        id,oran = tani.predict(gri[y:y+h,x:x+w])
        print(id)
        id = name[id]

        cv2.putText(cerceve,str(id)+"%"+str(oran),(x+5,y-5),font,1,(255,255,255),2)
    cv2.imshow('sonuc',cerceve)
    k = cv2.waitKey(100) & 0xFF
    if k == 27:
        break

cam.release()
cv2.destroyAllWindows()
