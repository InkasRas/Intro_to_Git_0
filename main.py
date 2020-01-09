from PyQt5 import uic
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random


class Example(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.clicked = False
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.clicked = True
        self.pushButton.setVisible(False)
        self.update()

    def paintEvent(self, evnt):
        if self.clicked:
            paint = QPainter()
            paint.begin(self)
            paint.setRenderHint(QPainter.Antialiasing)
            paint.setBrush(Qt.white)
            paint.drawRect(evnt.rect())
            paint.setPen(Qt.yellow)
            for k in range(random.randint(5, 20)):
                center = QPoint(random.randint(0, 1000), random.randint(0, 1000))
                paint.setBrush(Qt.yellow)
                d = random.randint(40, 150)
                paint.drawEllipse(center, d, d)
            paint.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
