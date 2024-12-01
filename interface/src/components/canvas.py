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

        print(self.width, self.height)
        pixmap = QtGui.QPixmap(self.width, self.height)
        pixmap.fill(Qt.white)
        self.setPixmap(pixmap)
        self.bitmap = [[False for _ in range(pixelWidth)] for _ in range(pixelHeight)]

        self.last_x, self.last_y = None, None
        self.drawingColor = QtGui.QColor('#000000')
        self.erasingColor = QtGui.QColor('#FFFFFF')
        self.drawingMode = True

        self.spacingMask = None
        self.showMask = False

    #set drawing mode (true if drawing, false if erasing)
    def setDrawingMode(self, currMode):
        self.drawingMode = currMode

    def __drawPixelAtPosWithColor(self,x,y,color):
        
        # print(x,y)
        #Set the bitmap equal to true if we are drawing on that pixel and false if we are erasing
        
        canvas = self.pixmap()
        painter = QtGui.QPainter(canvas)
        p = painter.pen()
        p.setWidth(self.pixelSize)
        p.setColor(color)
        painter.setPen(p)
        point = QPoint(x//self.pixelSize * self.pixelSize + self.pixelSize//2, y//self.pixelSize * self.pixelSize + self.pixelSize//2)
        painter.drawPoint(point)
        painter.end()
        self.setPixmap(canvas)

    def __drawPixelAtPos(self,x,y):
        if x < 0 or x // self.pixelSize >= len(self.bitmap[0]) or \
           y < 0 or y // self.pixelSize >= len(self.bitmap) or \
           self.bitmap[y // self.pixelSize][x // self.pixelSize] == self.drawingMode :
            return
        self.bitmap[y // self.pixelSize][x // self.pixelSize] = self.drawingMode 
        if self.spacingMask[y // self.pixelSize][x // self.pixelSize]:
            self.__drawPixelAtPosWithColor(x,y, self.maskDarkColor if self.drawingMode else self.maskLightColor)
        else:
            self.__drawPixelAtPosWithColor(x,y, self.drawingColor if self.drawingMode else self.erasingColor)
    

    def updateSpacingMask(self):
        lightColor = self.maskLightColor if self.showMask else self.erasingColor
        darkColor = self.maskDarkColor if self.showMask else self.drawingColor
        for i in range(len(self.spacingMask)):
            for j in range(len(self.spacingMask[0])):
                if self.spacingMask[i][j]:
                    self.__drawPixelAtPosWithColor(j*self.pixelSize, i*self.pixelSize, darkColor if self.bitmap[i][j] else lightColor)

    def setSpacingMask(self, spacingMask, lightColor, darkColor):
        self.spacingMask = spacingMask
        self.maskLightColor = QtGui.QColor(lightColor)
        self.maskDarkColor =QtGui.QColor(darkColor)
    
    def toggleDisplayMask(self):
        self.showMask = not self.showMask
        self.updateSpacingMask()
        


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