import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QSize
from components.canvas import Canvas
from components.buttons import QMenuButton
from pages.drawingPage import DrawingPage

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        drawingPage = DrawingPage()

        self.setFixedSize(QSize(600, 400))
        self.setCentralWidget(drawingPage)
    





app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()