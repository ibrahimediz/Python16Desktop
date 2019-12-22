import sys
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QMessageBox
from PyQt5.QtGui import QIcon
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 örnek window'
        self.left = 100  
        self.top = 100
        self.width = 640
        self.height = 480
        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This s an example button')
        button.move(100,70) 
        button.clicked.connect(self.on_click)
        self.show()        
    def on_click(self):
        elCevap = QMessageBox.question(self,"Soru","Ara Verelim mi?",\
            QMessageBox.Ok | QMessageBox.Yes | QMessageBox.YesToAll,\
                QMessageBox.Ok)
        if elCevap == QMessageBox.Ok:
            print("Ara Verelim")
        elif elCevap == QMessageBox.Yes:
            print("Ara Verelim 2")        
        elif elCevap == QMessageBox.YesToAll:
            print("Ara Verelim 3")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
