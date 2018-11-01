from PyQt5.QtWidgets import QMainWindow,  \
                            QApplication, \
                            QGridLayout, \
                            QWidget, \
                            QPushButton, \
                            QLabel, \
                            QMessageBox

import PyQt5.QtGui as QtGui
import sys


class gridPosition():
    def __init__(self, row=0, column=0, color="white"):
        self.row = row
        self.column = column
        self.color = "white"
        self.piecesInARow = 1

class Qt_window(QMainWindow):
    def __init__(self):
        super(Qt_window, self).__init__()
        self.initUI()
        self.show()  # have the main window appear onscreen
        self.playerTurn = "red"
        self.initBackgroundColor()
        self.matrix = self.initGameMatrix()  # create the matrix to store the current game state
        self.columnPieceCounts = self.initColumnPieceCounts()
        self.loopInitButtons()

    def initUI(self):
        self.grid = QGridLayout()  # create a grid layout for the buttons and labels
        self.mainWindow = QWidget(self)  # the main window is a Qwidget, a generic widget
        self.initGrid()
        self.setCentralWidget(self.mainWindow)  # set this main window as the basic widget of the app
        self.mainWindow.setLayout(self.grid)  # at the grid to the main window
        self.initBackgroundColor()

    def initGrid(self):
        for i in range(0, 7):
            self.grid.addWidget(QPushButton("Drop"), 1, i)  # create the row of buttons at the top of the grid
        for i in range(2, 8):
            for j in range(0, 7):
                self.grid.addWidget(QLabel(), i, j)
        for i in range(7, self.grid.count()):
            child = self.grid.itemAt(i).widget()
            # you can change the labels appearance with a CSS stylesheet
            child.setStyleSheet("background-color: white; border-radius: 10; border: 1px inset black; min-height: 40")

    def initBackgroundColor(self):
        palette = QtGui.QPalette()  # color options can be used with the Qpalette module
        palette.setColor(QtGui.QPalette.Background, QtGui.QColor("#99ccff"))  # create color palette for main window
        self.setPalette(palette)  # set the color for the main window

    def initGameMatrix(self):
        matrix = []
        for i in range(0, 6):
            newColumn = []
            for j in range(0, 7):
                newColumn.append("white")
            matrix.append(newColumn)
        return matrix

    def initColumnPieceCounts(self):
        counts = []  # initialize the array to track pieces in each column
        for i in range(0, 7):
            counts.append(0)
        return counts

    # connect the event (called slots in Qt) to each button press
    def loopInitButtons(self):
        for i in range(0, 7):
            button = self.grid.itemAt(i).widget()
            button.clicked.connect(self.connectionFactory(button))

    # this function is needed due to some wierd logic with lambda
    def connectionFactory(self, button):
        return lambda: self.dropPiece(button)

    def getGridWidget(self, row, column):
        if row > 6 or column > 7:
            print("Grid coordinates out of range")
            return None
        index = (row * 7) + column - 1
        return self.grid.itemAt(index).widget()

    def changeTurn(self):
        if self.playerTurn == "red":
            self.playerTurn = "blue"
        else:
            self.playerTurn = "red"

    def dropPiece(self, widget):
        column = self.grid.indexOf(widget)
        if self.columnPieceCounts[column] is not 6:
            self.columnPieceCounts[column] += 1
            row = self.columnPieceCounts[column]
            color = self.playerTurn
            self.matrix[row - 1][column] = color
            numberOfRowsIndex = 7
            self.getGridWidget(numberOfRowsIndex - row, column + 1).setStyleSheet("background-color:" + color + "; border-radius: 10; \
             border: 1px inset black; min-height: 40;")
            if self.checkIfGameOver():
                print(self.playerTurn + " won")
                self.popupGameOver()
                self.restartGame()
            else:
                self.changeTurn()

    def popupGameOver(self):
        msg = QMessageBox()
        msg.setWindowTitle("GAME OVER")
        msg.setText("Player " + self.playerTurn + " won")
        msg.exec_()

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
                if gridPos.inARowCount is 4:
                    return True

    def checkHorizontal(self):
        gridPos = gridPosition(0, 0)
        for row in range(0, 6):
            gridPos.row = row
            gridPos.color = self.matrix[gridPos.row][gridPos.column]
            while gridPos.column < 6:
                gridPos.column += 1
                gridPos = self.checkNextColor(gridPos)
                if gridPos.inARowCount is 4:
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
        while row in range(0, 6) and column in range(0, 6):
            gridPos = self.checkNextColor(gridPos)
            if gridPos.piecesInARow is 4:
                return True
            gridPos.row -= 1
            gridPos.column += 1

    def checkNextColor(self, gridPos):
        nextColor = self.matrix[gridPos.row][gridPos.column]
        if nextColor is gridPos.color and nextColor is not "white":
            gridPos.inARowCount += 1
        else:
            gridPos.inARowCount = 1
        gridPos.color = nextColor
        return gridPos

    def restartGame(self):
        for i in range(7, self.grid.count()):
            label = self.grid.itemAt(i).widget()
            label.setStyleSheet("background-color: white; border-radius: 10; \
             border: 1px inset black; min-height: 40;")
        self.matrix = self.initGameMatrix()
        for i in range(0, len(self.columnPieceCounts)):
            self.columnPieceCounts[i] = 0


if __name__ == "__main__":
    q_app = QApplication(sys.argv)
    q_window = Qt_window()
    sys.exit(q_app.exec())