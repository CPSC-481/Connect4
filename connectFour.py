from PyQt5.QtWidgets import QMainWindow,  \
                            QApplication, \
                            QGridLayout, \
                            QWidget, \
                            QPushButton, \
                            QLabel
import sys
from enum import Enum

class Colors(Enum):
    white = 0
    red = 1
    blue = 2

class Qt_window(QMainWindow):
    def __init__(self):
        super(Qt_window, self).__init__()
        self.grid = QGridLayout()
        self.mainWindow = QWidget(self)
        self.initGrid()
        self.setCentralWidget(self.mainWindow)
        self.mainWindow.setLayout(self.grid)
        self.show()
        self.matrix = self.initGameMatrix()

    def initGrid(self):
        for i in range(0, 7):
            self.grid.addWidget(QPushButton("Drop"), 1, i)
        for i in range(2, 8):
            for j in range(0, 7):
                self.grid.addWidget(QLabel(), i, j)
        for i in range(7, self.grid.count()):
            child = self.grid.itemAt(i).widget()
            child.setStyleSheet("background-color: white; border-radius: 10; border: 1px inset black; min-height: 40")
    def initGameMatrix
        matrix = []
        for i in range(0, 6):
            newColumn = []
            for j in range(0, 5):
                newColumn.append(Colors.white)
            matrix.append(newColumn)
        return matrix
if __name__ == "__main__":
    q_app = QApplication(sys.argv)
    q_window = Qt_window()
    sys.exit(q_app.exec())