import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLineEdit

class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        
        l = QtWidgets.QVBoxLayout()
        self.setLayout(l)
        l.addWidget(self.canvas)
        
