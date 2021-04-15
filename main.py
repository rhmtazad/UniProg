# import sys
#
# from PyQt5 import uic
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
#
#
# class UserInterface(QMainWindow):
#     def __init__(self):
#         super(UserInterface, self).__init__()
#         self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
#         self.setAttribute(Qt.WA_TranslucentBackground, True)
#         uic.loadUi('ui/main.ui', self)
#         self.center_window()
#
#     def center_window(self):
#         frame_geometry = self.frameGeometry()
#         center_point = QDesktopWidget().availableGeometry().center()
#         frame_geometry.moveCenter(center_point)
#         self.move(frame_geometry.topLeft())
#
#
# app = QApplication(sys.argv)
# user_interface = UserInterface()
# user_interface.show()
# app.exec()

import pandas as pd


from dataclasses import dataclass, field


@dataclass(order=True)
class UniProgCSV:
    index: str
    file: str
    columns: list[str] = field(default_factory=list)

    @property
    def columns_df(self):
        return pd.DataFrame(columns=self.columns).set_index(self.index)

    def data_df(self, data):
        return pd.DataFrame([data], columns=self.columns).set_index(self.index)

    def read(self):
        try:
            return pd.read_csv(f'{self.file}.csv', index_col=self.index)
        except FileNotFoundError:
            self.save(self.columns_df)
            return pd.read_csv(f'{self.file}.csv', index_col=self.index)

    def save(self, indexed_df):
        indexed_df.to_csv(f'{self.file}.csv')

    def append(self, data):
        self.save(self.read().append(self.data_df(data)))
