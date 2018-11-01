class gridPosition():
    def __init__(self, row=0, column=0, color="white"):
        self.row = row
        self.column = column
        self.color = "white"
        self.piecesInARow = 1

class gameOverChecker():
    def __init__(self, matrix):
        self.matrix = matrix

    def checkIfGameOver(self):
        if self.checkVerticals() or self.checkHorizontal() or \
                self.checkDiagonalDownUp() or self.checkDiagonalUpDown():
            return True
        return False

    def checkVerticals(self):
        gridPos = gridPosition(0, 0)
        for column in range(0, 7):
            gridPos.column = column
            gridPos.color = self.matrix[gridPos.row][gridPos.column]
            while gridPos.color is not "white" and gridPos.row in range(0, 5):
                gridPos.row += 1
                gridPos = self.checkNextColor(gridPos)
                if gridPos.piecesInARow is 4:
                    return True

    def checkHorizontal(self):
        gridPos = gridPosition(0, 0)
        for row in range(0, 6):
            gridPos.row = row
            gridPos.color = self.matrix[gridPos.row][gridPos.column]
            while gridPos.column < 6:
                gridPos.column += 1
                gridPos = self.checkNextColor(gridPos)
                if gridPos.piecesInARow is 4:
                    return True

    def checkDiagonalDownUp(self):
        for row in range(0, 3):
            if self.upDiagonalHelper(row, 0):
                return True
        for column in range(1, 4):
            if self.upDiagonalHelper(0, column):
                return True
        return False

    def upDiagonalHelper(self, row, column):
        gridPos = gridPosition(row, column, self.matrix[row][column])
        while gridPos.column in range(0, 6) and gridPos.row in range(0, 5):
            gridPos = self.checkNextColor(gridPos)
            if gridPos.piecesInARow is 4:
                return True
            gridPos.row += 1
            gridPos.column += 1

    def checkDiagonalUpDown(self):
        for row in range(3, 6):
            if self.downDiagonalHelper(row, 0):
                return True
        for column in range(0, 3):
            if self.downDiagonalHelper(5, column):
                return True
        return False

    def downDiagonalHelper(self, row, column):
        gridPos = gridPosition(row, column, self.matrix[row][column])
        while gridPos.row in range(0, 6) and gridPos.column in range(0, 7):
            gridPos = self.checkNextColor(gridPos)
            if gridPos.piecesInARow is 4:
                return True
            gridPos.row -= 1
            gridPos.column += 1

    def checkNextColor(self, gridPos):
        nextColor = self.matrix[gridPos.row][gridPos.column]
        if nextColor is gridPos.color and nextColor is not "white":
            gridPos.piecesInARow += 1
        else:
            gridPos.piecesInARow = 1
        gridPos.color = nextColor
        return gridPos