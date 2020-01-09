from PyQt5 import uic
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random


class Example(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1000, 1000)
        self.pushButton = QPushButton('PUSH', self)
        self.pushButton.resize(150, 150)
        self.pushButton.move(50, 50)
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
            col = QColor(random.randint(0, 255),
                         random.randint(0, 255),
                         random.randint(0, 255))
            paint.setPen(col)
            for k in range(random.randint(5, 20)):
                center = QPoint(random.randint(0, 1000), random.randint(0, 1000))
                col = QColor(random.randint(0, 255),
                             random.randint(0, 255),
                             random.randint(0, 255))
                paint.setBrush(col)
                d = random.randint(40, 150)
                paint.drawEllipse(center, d, d)
            paint.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
