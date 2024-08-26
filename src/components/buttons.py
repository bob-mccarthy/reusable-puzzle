import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

class QMenuButton(QtWidgets.QPushButton):

    def __init__(self, text):
        super().__init__()
        self.setFixedSize(QtCore.QSize(100,30))
        self.setText(text)
        # self.color = color
        # self.setStyleSheet("background-color: %s;" % color)
    