import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QComboBox
from components.canvas import Canvas
from components.buttons import QMenuButton
from puzzle import Puzzle
NUM_PIECES_COL = 3 
NUM_PIECES_ROW = 4 
X_SPACING = 1
Y_SPACING = 1 
RES = 4 #1 is full resolution and resolution of x is pixels / x
class DrawingPage(QWidget):
    def __init__(self):
        super().__init__()

        
        self.canvas = Canvas(128//RES*NUM_PIECES_COL, 64//RES*NUM_PIECES_ROW, 10)
        puzzle = Puzzle(NUM_PIECES_COL, NUM_PIECES_ROW, RES)

        l = QtWidgets.QVBoxLayout()
        self.setLayout(l)

        topRow = QtWidgets.QHBoxLayout()
        topRow.addWidget(self.canvas)

        optionsCol = QtWidgets.QVBoxLayout()
        viewSelector = QComboBox()
        puzzlePieces = ['ALL']
        puzzlePieces.extend([f'Puzzle Piece: {i + 1}' for i in range(NUM_PIECES_COL * NUM_PIECES_ROW)])

        viewSelector.addItems(puzzlePieces)
        optionsCol.addWidget(viewSelector)
        topRow.addLayout(optionsCol)
        l.addLayout(topRow)
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
        # puzzle.printPuzzlePieces()
        print(puzzle.puzzlePiecesToBinary())
