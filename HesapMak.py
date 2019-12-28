import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton
from PyQt5 import uic
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.win = uic.loadUi("GUI/HesapMak.ui",self)
        for i in range(0,10):
            self.findChild(QPushButton,"b"+str(i)).clicked.connect(self.tiklandi)
        # self.win.txtSonuc.textChanged.connect(self.temizle)
        self.win.show()        

    def tiklandi(self):
        dugme = self.sender()
        self.win.txtSonuc.setText(dugme.text())

    def temizle(self):
        sonuc = list(self.win.txtSonuc.text())
        for i in sonuc:
            if not i.isdigit():
                sonuc.remove(i)
        temiz = ""
        temiz = temiz.join(sonuc)
        self.win.txtSonuc.setText(temiz)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
