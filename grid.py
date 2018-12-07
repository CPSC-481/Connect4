from PyQt5.QtWidgets import QGridLayout, \
                            QPushButton, \
                            QLabel


class gridLayout:
    def __init__(self):
        self.layout = QGridLayout()  # create a grid layout for the buttons and labels
        self.createButtonRow()
        self.createLabels()

    def createButtonRow(self):
        for i in range(0, 7):
            self.layout.addWidget(QPushButton("Drop"), 1, i)  # create the row of buttons at the top of the grid

    def createLabels(self):
        self.addLabelWidgets()
        self.setLabelStyleSheets()

    def addLabelWidgets(self):
        for i in range(2, 8):
            for j in range(0, 7):
                self.layout.addWidget(QLabel(), i, j)

    def setLabelStyleSheets(self):
        for i in range(7, self.layout.count()):
            child = self.layout.itemAt(i).widget()
            # you can change the labels appearance with a CSS stylesheet
            child.setStyleSheet("background-color: white; border-radius: 21; border: 1px inset black;"
                                " min-height: 40; min-width: 40")

    # connect the event (called slots in Qt) to each button press
    def loopInitButtons(self, callback):
        for i in range(0, 7):
            button = self.layout.itemAt(i).widget()
            button.clicked.connect(self.connectionFactory(button, callback))

    # this function is needed due to some weird logic with lambda
    # if lambda is used in connect above, it ony instantiates once, with the last button instance
    # this function ensures a new lambda instance for each button
    def connectionFactory(self, button, callback):
        return lambda: callback(button)

    def getGridWidget(self, row, column):
        if row > 6 or column > 7:
            print("Grid coordinates out of range")
            return None
        index = (row * 7) + column - 1
        return self.layout.itemAt(index).widget()
