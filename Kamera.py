from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic
from PyQt5.QtCore import QTimer
import cv2
from PyQt5.QtGui import QImage,QPixmap
import numpy as np
from PIL import Image
import os,json
import sys

class Kamera(QMainWindow):
    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.win = uic.loadUi("GUI/Kamera1.ui",self)
        self.initUI()
    
    def initUI(self):
        self.win.btKamera.clicked.connect(self.btClick)
        self.win.btKapat.clicked.connect(self.kapat)
        self.win.show()

    def btClick(self):
        if not self.timer.isActive():
            self.cam = cv2.VideoCapture(0)
            self.timer.start(3)
            self.KameraAc()

    def kapat(self):
        self.cam.release()
        self.timer.stop()
    
    def KameraAc(self):
        
        faceDec = cv2.CascadeClassifier(r"Opencv\cascades\haarcascade_frontalface_default.xml")

        say = 0
        while 1:
            ret,frame = self.cam.read()
            image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            h,w,c = image.shape
            step = c*w
            gri = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = faceDec.detectMultiScale(gri,1.7,5)
            qImg = QImage(image.data,w,h,step,QImage.Format_RGB888)
            self.win.kamera.setPixmap(QPixmap.fromImage(qImg))
            for (x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                path =  os.getcwd()+os.sep+"dataset"+os.sep+"Ali"+os.sep+str(say)+".jpg"
                cv2.imwrite(path,gri[y:y+h,x:x+w]) 
                say += 1 
            k = cv2.waitKey(5) & 0xFF
            if k == 27 or say >= 300:
                break
        self.cam.release()
        self.timer.stop()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Kamera()
    sys.exit(app.exec_())

