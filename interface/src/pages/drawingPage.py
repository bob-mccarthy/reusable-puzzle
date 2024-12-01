import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QComboBox
from components.canvas import Canvas
from components.buttons import QMenuButton
from puzzle import Puzzle
NUM_PIECES_COL = 2 
NUM_PIECES_ROW = 3
X_SPACING = 12 #dimension in pixels
Y_SPACING = 12 #dimension in pixels
PIXEL_SIZE = 10
RES = 4 #1 is full resolution and resolution of x is pixels / x
class DrawingPage(QWidget):
    def __init__(self):
        super().__init__()

        
        self.canvas = Canvas((128//RES)*NUM_PIECES_COL + ( X_SPACING // RES) * (NUM_PIECES_COL - 1) \
                             , (64//RES)*NUM_PIECES_ROW + (Y_SPACING // RES) * (NUM_PIECES_ROW - 1) \
                             , PIXEL_SIZE)
        puzzle = Puzzle(NUM_PIECES_COL, NUM_PIECES_ROW,X_SPACING, Y_SPACING, RES, [128//RES, 64//RES])
        self.generateSpacingMask()
        l = QtWidgets.QVBoxLayout()
        self.setLayout(l)
        self.canvas.setSpacingMask(self.generateSpacingMask(), '#bababa', '#545454')
        # self.canvas.displayOverlay(self.generateSpacingMask(), '#000000')

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
        toggle = QMenuButton('Toggle Mask')
        toggle.clicked.connect(self.canvas.toggleDisplayMask) 
        clear.clicked.connect(self.canvas.clearCanvas) 
        send = QMenuButton('Send')
        send.clicked.connect(lambda : self.__copyAndPrint(puzzle))
        buttonRow.addWidget(erase)
        buttonRow.addWidget(draw)
        buttonRow.addWidget(clear)
        buttonRow.addWidget(toggle)
        buttonRow.addWidget(send)
        
        
        
        l.addLayout(buttonRow)

    def __copyAndPrint(self, puzzle):
        puzzle.loadBitmap(self.canvas.getBitMapCopy()) 
    
        
    #generates a bitmap that is true if that image with not appear on the puzzle 
    def generateSpacingMask(self):
        bitmapWidth = (128//RES)*NUM_PIECES_COL + ( X_SPACING // RES) * (NUM_PIECES_COL - 1)
        bitmapHeight = (64//RES)*NUM_PIECES_ROW + (Y_SPACING // RES) * (NUM_PIECES_ROW - 1)
        puzzleWidth = 128//RES 
        puzzleHeight = 64//RES
        bitmap = [[False for x in range(bitmapWidth)] for y in range(bitmapHeight)]
        print(bitmapWidth, bitmapHeight)
        numWriting = 0

        #iterate across all of the rows that are apart of the spacing mask
        for i in range(1, NUM_PIECES_ROW):
            spacingStart = puzzleHeight * i  + Y_SPACING//RES * (i - 1)
            for j in range(spacingStart, Y_SPACING//RES+spacingStart):
                for k in range(bitmapWidth):
                    bitmap[j][k] = True
        # #iterate across all of the cols that are apart of the spacing mask
        for i in range(1, NUM_PIECES_COL):
            spacingStart = puzzleWidth * i + X_SPACING//RES * (i - 1)
            for j in range(spacingStart, X_SPACING//RES+spacingStart):
                for k in range(bitmapHeight):
                    bitmap[k][j] = True
        return bitmap




