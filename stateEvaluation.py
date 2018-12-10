def evaluateState(state, playerColor):
    totalHeuristicValue = 0
    totalHeuristicValue += applyHeuristicHorizontally(state, playerColor)
    totalHeuristicValue += applyHeuristicVertically(state, playerColor)
    totalHeuristicValue += applyHeuristicDiagonalDownUp(state, playerColor)
    totalHeuristicValue += applyHeuristicDiagonalUpDown(state, playerColor)
    return totalHeuristicValue


class Bubble:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.values = []


def applyHeuristicHorizontally(state, playerColor):
    val = 0
    for row in range(0, 6):
        for column in range(0, 4):
            bubble = Bubble(row, column)
            val += horizontalAndVerticalHelper(bubble, state, playerColor, True)
    return val


def applyHeuristicVertically(state, playerColor):
    val = 0
    for column in range(0, 7):
        for row in range(0, 3):
            bubble = Bubble(row, column)
            val += horizontalAndVerticalHelper(bubble, state, playerColor, False)
    return val


def horizontalAndVerticalHelper(bubble, state, playerColor, isHorizontal):
    for i in range(0, 4):
        bubble.values.append(state.matrix[bubble.row][bubble.column])
        if isHorizontal:
            bubble.column += 1
        else:
            bubble.row += 1
    return evaluateBubbles(bubble.values, playerColor)


def applyHeuristicDiagonalDownUp(state, playerColor):
    val = 0
    for row in range(0, 4):
        bubble = Bubble(row, 0)
        while bubble.row < 3 and bubble.column < 4:
            val += getValAndIncrementBubblePosition(bubble, state, playerColor, True)
    for column in range(1, 5):
        bubble = Bubble(0, column)
        while bubble.row < 3 and bubble.column < 4:
            val += getValAndIncrementBubblePosition(bubble, state, playerColor, True)
    return val


def applyHeuristicDiagonalUpDown(state, playerColor):
    val = 0
    for row in range(3, 6):
        bubble = Bubble(row, 0)
        while bubble.row > 2 and bubble.column < 4:
            val += getValAndIncrementBubblePosition(bubble, state, playerColor, False)
    for column in range(1, 4):
        bubble = Bubble(5, column)
        while bubble.row > 2 and bubble.column < 4:
            val += getValAndIncrementBubblePosition(bubble, state, playerColor, False)
    return val


def getValAndIncrementBubblePosition(bubble, state, color, isDownUp):
    bubble.values = []
    for i in range(0, 4):
        rowVal = bubble.row + i
        if not isDownUp:
            rowVal = bubble.row - i
        bubble.values.append(state.matrix[rowVal][bubble.column + i])
    val = evaluateBubbles(bubble.values, color)
    bubble.column += 1
    if isDownUp:
        bubble.row += 1
    else:
        bubble.row -= 1
    return val


def evaluateBubbles(bubble, playerColor):
    colorEncountered = "white"
    colorCount = 0
    for color in bubble:
        if color is not colorEncountered:
            if colorEncountered is not "white":
                if color is not "white":
                    return 0
            else:
                colorCount += 1
                colorEncountered = color
        else:
            if color is not "white":
                colorCount += 1
    if colorCount is 0:
        return 1
    val = 2 ** colorCount
    if colorCount is 4:
        val = float("inf")
    if colorEncountered is not playerColor:
        val = -val
    return val
