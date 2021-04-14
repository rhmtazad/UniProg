import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class UserInterface(QMainWindow):
    def __init__(self):
        super(UserInterface, self).__init__()
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        uic.loadUi('main.ui', self)

        self.show()


app = QApplication(sys.argv)
user_interface = UserInterface()
app.exec()
