from PyQt5.QtWidgets import QMainWindow,  \
                            QApplication, \
                            QWidget, \
                            QMessageBox

import PyQt5.QtGui as QtGui
import sys
from grid import gridLayout
from gameOverChecker import gameOverChecker


class Qt_window(QMainWindow):
    def __init__(self):
        super(Qt_window, self).__init__()
        self.initUI()
        self.show()  # have the main window appear onscreen
        self.playerTurn = "red"
        self.initBackgroundColor()
        self.matrix = self.initGameMatrix()  # create the matrix to store the current game state
        self.columnPieceCounts = self.initColumnPieceCounts()
        self.grid.loopInitButtons(self.dropPiece)

    def initUI(self):
        self.grid = gridLayout()  # create a grid layout for the buttons and labels
        self.mainWindow = QWidget(self)  # the main window is a Qwidget, a generic widget
        self.setCentralWidget(self.mainWindow)  # set this main window as the basic widget of the app
        self.mainWindow.setLayout(self.grid.layout)  # at the grid to the main window
        self.initBackgroundColor()

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

    def changeTurn(self):
        if self.playerTurn == "red":
            self.playerTurn = "blue"
        else:
            self.playerTurn = "red"

    def dropPiece(self, widget):
        column = self.grid.layout.indexOf(widget)
        if self.columnPieceCounts[column] is not 6:
            self.columnPieceCounts[column] += 1
            row = self.columnPieceCounts[column]
            color = self.playerTurn
            self.matrix[row - 1][column] = color
            numberOfRowsIndex = 7
            self.grid.getGridWidget(numberOfRowsIndex - row, column + 1).setStyleSheet("background-color:" + color + "; border-radius: 10; \
             border: 1px inset black; min-height: 40;")
            if self.isGameOver():
                print(self.playerTurn + " won")
                self.popupGameOver()
                self.restartGame()
            else:
                self.changeTurn()

    def isGameOver(self):
        checker = gameOverChecker(self.matrix)
        return checker.checkIfGameOver()

    def popupGameOver(self):
        msg = QMessageBox()
        msg.setWindowTitle("GAME OVER")
        msg.setText("Player " + self.playerTurn + " won")
        msg.exec_()

    def restartGame(self):
        for i in range(7, self.grid.layout.count()):
            label = self.grid.layout.itemAt(i).widget()
            label.setStyleSheet("background-color: white; border-radius: 10; \
             border: 1px inset black; min-height: 40;")
        self.matrix = self.initGameMatrix()
        for i in range(0, len(self.columnPieceCounts)):
            self.columnPieceCounts[i] = 0


if __name__ == "__main__":
    q_app = QApplication(sys.argv)
    q_window = Qt_window()
    sys.exit(q_app.exec())