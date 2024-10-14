class Puzzle:
    #puzzlePieces: a list where puzzlePieces where puzzlePieces[i][j] is a 2D list of booleans representing true is the pixel is on and false if off
    #   also each puzzle piece represents one OLED screen   
    #size: an integer that tells the number of puzzle rows/cols (it has to be a square puzzle) 
    #resolution 
    def __init__(self, size,resolution):
        self.puzzlePieces = []
        self.size = size
        self.resolution = resolution
    #loadBitmap: a function which loads the bitmap into the puzzlePieces list 
    # bitmap: the image in a 2D boolean list where true is black and false is white
    def loadBitmap(self, bitmap):
        self.puzzlePieces = []
        height = len(bitmap)
        width = len(bitmap[0])
        print(height)
        print(width)
        for i in range(self.size):
            row = []
            for j in range(self.size):
                print(f'height {int(height*(i/self.size)),int(height*((i+1)/self.size))}')
                # print(f'width parameters {width, j, self.size}')
                print(f'width {int(width*(j/self.size)),int(width*((j+1)/self.size))}')
                row.append([r[int(width*(j/self.size)):int(width*((j+1)/self.size))] for r in bitmap[int(height*(i/self.size)):int(height*((i+1)/self.size))]] )
            self.puzzlePieces.append(row)

    #converts the list of puzzle pieces into a list of lists of binary strings 
    #   each string is 8 bit and start from bottom right to top left (as 0,0 on the OLED screen is the bottom left 8 pixels)
    def puzzlePiecesToBinary(self):
        print('in puzzle')
        newPieces = []
        for i in range(len(self.puzzlePieces)):
            for j in range(len(self.puzzlePieces[i])):
                puzzleWidth = len(self.puzzlePieces[i][j][0]) 
                puzzleHeight = len(self.puzzlePieces[i][j]) 
                newPiece = [[0 for y in range(puzzleWidth * self.resolution)] for x in range(puzzleHeight * self.resolution)]
                for k in range(len(self.puzzlePieces[i][j])):
                    for l in range(len(self.puzzlePieces[i][j][k])):
                        for m in range(k * 4, (k+1) * 4):
                            for n in range(l * 4, (l + 1) * 4):
                                newPiece[m][n] = self.puzzlePieces[i][j][k][l]
                newPieces.append(newPiece)
        puzzlePieceStrs = []
        for i in range(len(newPieces)):
            
                binaryStrs = []
                for l in reversed(range(len(newPieces[i][0]))):
                    for k in reversed(range(len(newPieces[i])// 8)):
                        binaryStr = []
                        for m in range(8):
                            binaryStr.append('1' if newPieces[i][k*8 + m][l] else '0')
                        print(binaryStr)
                        binaryStrs.append(''.join(binaryStr))
                puzzlePieceStrs.append(binaryStrs)
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

        
            