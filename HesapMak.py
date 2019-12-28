import sys
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton
from PyQt5 import uic
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sayi1 = 0
        self.sayi2 = 0
        self.islem = 0
        self.bitti = 0
        self.win = uic.loadUi("GUI/HesapMak.ui",self)
        self.initUI()
        self.win.show()        


    def initUI(self):
        self.win.keyPressEvent = self.tusBas
        for i in range(0,10):
                self.findChild(QPushButton,"b"+str(i)).clicked.connect(self.tiklandi)
        liste = ["Arti","Bol","Carp","Eksi"]
        for item in liste:
            self.findChild(QPushButton,"bt"+str(item)).clicked.connect(self.islemyap)
        self.win.btEsit.clicked.connect(self.esittir)
        self.win.btTemizle.clicked.connect(self.temizleBt)
        self.win.txtSonuc.textChanged.connect(self.temizle)


    def tusBas(self,event):
        print(int(event.key())-48,(event.key()))

    def islemyap(self):
        dugme = self.sender()
        self.sayi1 = self.txtSonuc.text()
        self.win.txtSonuc.setText("")
        self.islem = dugme.text()

    def tiklandi(self):
        dugme = self.sender()
        if self.bitti == 1:
            self.win.txtSonuc.setText("")
            self.bitti = 0
        yazilacak = self.win.txtSonuc.text() + dugme.text()
        self.win.txtSonuc.setText(yazilacak)

    def temizleBt(self):
        self.sayi1 = 0
        self.sayi2 = 0
        self.islem = 0
        self.bitti = 0
        self.win.txtSonuc.setText("0")


    def esittir(self):
        self.sayi2 = self.win.txtSonuc.text()
        islem = self.sayi1 + self.islem + self.sayi2
        self.win.txtSonuc.setText(str(eval(islem)))
        self.bitti = 1


    def temizle(self):
        try:
            sayi = self.win.txtSonuc.text()
            sayi = int(sayi)
            self.win.txtSonuc.setText(str(sayi))
        except:
            pass
        # sonuc = list(self.win.txtSonuc.text())
        # for i in sonuc:
        #     if not i.isdigit():
        #         sonuc.remove(i)
        # temiz = ""
        # temiz = temiz.join(sonuc)
        # self.win.txtSonuc.setText(temiz)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
