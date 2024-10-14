import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QPoint

PIXEL_LEN_IN_MM = 5

class Canvas(QtWidgets.QLabel):

    def __init__(self, pixelWidth, pixelHeight, pixelSize):
        super().__init__()
        
        self.pixelSize = pixelSize
        self.width = pixelWidth * pixelSize
        self.height = pixelHeight * pixelSize
        # print(width, height)
        pixmap = QtGui.QPixmap(self.width, self.height)
        pixmap.fill(Qt.white)
        self.setPixmap(pixmap)
        self.bitmap = [[False for _ in range(pixelWidth)] for _ in range(pixelHeight)]

        self.last_x, self.last_y = None, None
        self.drawingColor = QtGui.QColor('#000000')
        self.erasingColor = QtGui.QColor('#FFFFFF')
        self.drawingMode = True

    #set drawing mode (true if drawing, false if erasing)
    def setDrawingMode(self, currMode):
        self.drawingMode = currMode


    def __drawPixelAtPos(self,x,y):
        if x < 0 or x // self.pixelSize >= len(self.bitmap[0]) and \
           y < 0 or y // self.pixelSize >= len(self.bitmap) and \
           self.bitmap[y // self.pixelSize][x // self.pixelSize] == self.drawingMode :
            return
        #Set the bitmap equal to true if we are drawing on that pixel and false if we are erasing
        self.bitmap[y // self.pixelSize][x // self.pixelSize] = self.drawingMode 
        canvas = self.pixmap()
        painter = QtGui.QPainter(canvas)
        p = painter.pen()
        p.setWidth(self.pixelSize)
        p.setColor(self.drawingColor if self.drawingMode else self.erasingColor)
        painter.setPen(p)
        point = QPoint(x//self.pixelSize * self.pixelSize + self.pixelSize//2, y//self.pixelSize * self.pixelSize + self.pixelSize//2)
        painter.drawPoint(point)
        painter.end()
        self.setPixmap(canvas)


    def mousePressEvent(self, e):

        self.__drawPixelAtPos(e.x(), e.y())

    def mouseMoveEvent(self, e):

        self.__drawPixelAtPos(e.x(), e.y())

    
    def clearCanvas(self):
        for i in range(len(self.bitmap)):
            for j in range(len(self.bitmap[0])):
                self.bitmap[i][j] = False
        pixmap = QtGui.QPixmap(self.width, self.height)
        pixmap.fill(Qt.white)
        self.setPixmap(pixmap)

    def printBitMap(self):
        for row in self.bitmap:
            for pixel in row:
                print('#' if pixel else ' ' , end = '')
            print()
    def getBitMapCopy(self):
        bitmapCopy = []
        for row in self.bitmap:
            bitmapCopy.append(row[:])
        return bitmapCopy

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None