class Puzzle:
    #puzzlePieces: a list where puzzlePieces where puzzlePieces[i][j] is a 2D list of booleans representing true is the pixel is on and false if off
    #   also each puzzle piece represents one OLED screen   
    #size: an integer that tells the number of puzzle rows/cols (it has to be a square puzzle) 
    #resolution 
    def __init__(self, numCols, numRows,resolution):
        self.puzzlePieces = []
        self.numCols = numCols
        self.numRows = numRows
        self.resolution = resolution
    #loadBitmap: a function which loads the bitmap into the puzzlePieces list 
    # bitmap: the image in a 2D boolean list where true is black and false is white
    def loadBitmap(self, bitmap):
        self.puzzlePieces = []
        height = len(bitmap)
        width = len(bitmap[0])
        print(height)
        print(width)
        for i in range(self.numRows):
            row = []
            for j in range(self.numCols):
                print(f'height {int(height*(i/self.numRows)),int(height*((i+1)/self.numRows))}')
                # print(f'width parameters {width, j, self.size}')
                print(f'width {int(width*(j/self.numCols)),int(width*((j+1)/self.numCols))}')
                row.append([r[int(width*(j/self.numCols)):int(width*((j+1)/self.numCols))] for r in bitmap[int(height*(i/self.numRows)):int(height*((i+1)/self.numRows))]] )
            self.puzzlePieces.append(row)

    #converts the list of puzzle pieces into a list of lists of binary strings 
    #   each string is 8 bit and start from bottom right to top left (as 0,0 on the OLED screen is the bottom left 8 pixels)
    def puzzlePiecesToBinary(self):
        print('in puzzle')
        newPieces = []
        print(len(self.puzzlePieces), len(self.puzzlePieces[0]))
        for i in range(len(self.puzzlePieces)):
            for j in range(len(self.puzzlePieces[i])):
                puzzleWidth = len(self.puzzlePieces[i][j][0]) 
                puzzleHeight = len(self.puzzlePieces[i][j]) 
                newPiece = [[0 for y in range(puzzleWidth * self.resolution)] for x in range(puzzleHeight * self.resolution)]
                for k in range(len(self.puzzlePieces[i][j])):
                    for l in range(len(self.puzzlePieces[i][j][k])):
                        for m in range(k * self.resolution, (k+1) * self.resolution):
                            for n in range(l * self.resolution, (l + 1) * self.resolution):
                                newPiece[m][n] = self.puzzlePieces[i][j][k][l]
                newPieces.append(newPiece)
        puzzlePieceStrs = []
        print(len(newPieces[i][0]), len(newPieces[i])// 8)
        for i in range(len(newPieces)):
            
                binaryStrs = []
                for k in reversed(range(len(newPieces[i])// 8)):
                    for l in reversed(range(len(newPieces[i][0]))):
                        binaryStr = []
                        for m in range(8):
                            # print(k*8 + m, l)
                            binaryStr.append('1' if newPieces[i][k*8 + m][l] else '0')
                        # print(binaryStr)
                        binaryStrs.append('0b' + ''.join(binaryStr))
                puzzlePieceStrs.append(binaryStrs)
        print(len(puzzlePieceStrs[0]))
        return puzzlePieceStrs
        # for binaryStr in binaryStrs:
        #     print(binaryStr)

        

    def printPuzzlePieces(self):
        for i in range(len(self.puzzlePieces)):
            for j in range(len(self.puzzlePieces[i])):
                print(f'puzzle piece {i,j}')
                print('-' * (len(self.puzzlePieces[i][j][0])+ 2))
                for row in self.puzzlePieces[i][j]:
                    print('|', end = '')
                    for pixel in row:
                        print('#' if pixel else ' ' , end = '')
                    print('|', end = '')
                    print()
                print('-' * (len(self.puzzlePieces[i][j][0])+ 2))

        
            