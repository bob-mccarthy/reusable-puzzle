class Puzzle:
    
    # size: an integer that tells the number of puzzle rows/cols (it has to be a square puzzle) 
    def __init__(self, size):
        self.puzzlePieces = []
        self.size = size

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
                row.append([row[int(width*(j/self.size)):int(width*((j+1)/self.size))] for row in bitmap[int(height*(i/self.size)):int(height*((i+1)/self.size))]] )
            self.puzzlePieces.append(row)

    
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
        
            