import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QPoint

PIXEL_LEN_IN_MM = 5

class Canvas(QtWidgets.QLabel):

    def __init__(self, pixelWidth, pixelHeight, pixelSize):
        super().__init__()
        pixmap = QtGui.QPixmap(600, 300)
        pixmap.fill(Qt.white)
        self.setPixmap(pixmap)
        self.pixelSize = pixelSize
        width = pixelWidth * pixelSize
        height = pixelHeight * pixelSize
        self.bitmap = [[False for _ in range(pixelWidth)] for _ in range(pixelHeight)]

        self.last_x, self.last_y = None, None
        self.drawingColor = QtGui.QColor('#000000')
        self.erasingColor = QtGui.QColor('#FFFFFF')
        self.drawingMode = True

    #set drawing mode (true if drawing, false if erasing)
    def setDrawingMode(self, currMode):
        self.drawingMode = currMode


    def __drawPixelAtPos(self,x,y):
        if self.bitmap[y // self.pixelSize][x // self.pixelSize] == self.drawingMode:
            return
        #Set the bitmap equal to true if we are drawing on that pixel and false if we are erasing
        self.bitmap[y // self.pixelSize][x // self.pixelSize] = self.drawingMode 
        canvas = self.pixmap()
        painter = QtGui.QPainter(canvas)
        p = painter.pen()
        p.setWidth(self.pixelSize)
        p.setColor(self.drawingColor if self.drawingMode else self.erasingColor)
        painter.setPen(p)
        point = QPoint(x//20 * 20, y//20 * 20)
        painter.drawPoint(point)
        painter.end()
        self.setPixmap(canvas)


    def mousePressEvent(self, e):
        self.__drawPixelAtPos(e.x(), e.y())

    def mouseMoveEvent(self, e):
        self.__drawPixelAtPos(e.x(), e.y())

    
    def clearCanvas(self):
        pixmap = QtGui.QPixmap(600, 300)
        pixmap.fill(Qt.white)
        self.setPixmap(pixmap)

    def printBitMap(self):
        for row in self.bitmap:
            for pixel in row:
                print('#' if pixel else ' ' , end = '')
            print()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None