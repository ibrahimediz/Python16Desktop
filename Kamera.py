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
        while 1:
            ret,image = self.cam.read()
            image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
            h,w,c = image.shape
            
            step = c*w
            qImg = QImage(image.data,w,h,step,QImage.Format_RGB888)
            self.win.kamera.setPixmap(QPixmap.fromImage(qImg))
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break
        self.cam.release()
        self.timer.stop()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Kamera()
    sys.exit(app.exec_())

