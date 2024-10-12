import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from components.canvas import Canvas
from components.buttons import QMenuButton
from puzzle import Puzzle

class DrawingPage(QWidget):
    def __init__(self):
        super().__init__()

        
        self.canvas = Canvas(50, 50, 10)
        puzzle = Puzzle(3)

        l = QtWidgets.QVBoxLayout()
        self.setLayout(l)
        l.addWidget(self.canvas)
        buttonRow = QtWidgets.QHBoxLayout()
        erase = QMenuButton('Erase')
        erase.clicked.connect(lambda : self.canvas.setDrawingMode(False)) 
        draw = QMenuButton('Draw')
        draw.clicked.connect(lambda : self.canvas.setDrawingMode(True)) 
        clear = QMenuButton('Clear')
        clear.clicked.connect(self.canvas.clearCanvas) 
        send = QMenuButton('Send')
        send.clicked.connect(lambda : self.__copyAndPrint(puzzle))
        buttonRow.addWidget(erase)
        buttonRow.addWidget(draw)
        buttonRow.addWidget(clear)
        buttonRow.addWidget(send)
        
        
        l.addLayout(buttonRow)

    def __copyAndPrint(self, puzzle):
        puzzle.loadBitmap(self.canvas.getBitMapCopy()) 
        puzzle.printPuzzlePieces()
