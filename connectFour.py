from PyQt5.QtWidgets import QMainWindow,  \
                            QApplication, \
                            QWidget, \
                            QMessageBox

import PyQt5.QtGui as QtGui
import sys
from grid import gridLayout
from gameOverChecker import gameOverChecker
from naryTree import State, StateTree, swapTurnColor
from stateEvaluation import evaluateState

START_PLAYER = "yellow"

class Qt_window(QMainWindow):
    def __init__(self):
        super(Qt_window, self).__init__()
        self.initUI()
        self.show()  # have the main window appear onscreen
        self.playerTurn = START_PLAYER
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
        palette.setColor(QtGui.QPalette.Background, QtGui.QColor("#185dcc"))  # create color palette for main window
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
            self.playerTurn = "yellow"
        else:
            self.playerTurn = "red"

    def dropPiece(self, widget):
        column = self.grid.layout.indexOf(widget)
        if self.columnPieceCounts[column] < 7:
            self.columnPieceCounts[column] += 1
            row = self.columnPieceCounts[column]
            self.matrix[row - 1][column] = self.playerTurn
            self.grid.getGridWidget(7 - row, column + 1).setStyleSheet("background-color:" +
                            self.playerTurn + "; border-radius: 21; border: 1px inset black; height: 20; width: 20;")
            if self.isGameOver():
                self.popupGameOver()
                self.restartGame()
            else:
                self.changeTurn()
        testState = State(None, self.matrix, self.columnPieceCounts)
        testStateTree = StateTree(testState, 5, swapTurnColor(self.playerTurn))
        val = evaluateState(testStateTree.leafs[0], self.playerTurn)
        print("SUCCESS!", val)
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
            label.setStyleSheet("background-color: white; border-radius: 21; \
             border: 1px inset black; min-height: 40;")
        self.matrix = self.initGameMatrix()
        for i in range(0, len(self.columnPieceCounts)):
            self.columnPieceCounts[i] = 0


if __name__ == "__main__":
    q_app = QApplication(sys.argv)
    q_window = Qt_window()
    sys.exit(q_app.exec())