import sys

from PyQt5 import QtWidgets
from PyQt5.uic import loadUiType

main_window, _ = loadUiType('main.ui')


class MainApp(QtWidgets.QMainWindow, main_window):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

    def center_window(self):
        frame_geometry = self.frameGeometry()
        center_point = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
