from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Okienko(QMainWindow):
    def __init__(self):
        super(Okienko, self).__init__()
        self.setGeometry(400, 400, 300, 100)
        self.setWindowTitle("statki kurwa")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Sranie")
        self.label.move(130,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Nie zesraj się")
        self.b1.clicked.connect(self.klikk)

    def klikk(self):
        self.label.setText("spierdalaj")
        self.update()
        
    def update(self):
        self.label.adjustSize()



def window():
    app = QApplication(sys.argv)
    win = Okienko()



    win.show()
    sys.exit(app.exec_())

window()