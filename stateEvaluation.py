def evaluateState(state, playerColor):
    totalHeuristicValue = 0
    totalHeuristicValue += applyHeuristicHorizontally(state, playerColor), \
                           applyHeuristicVertically(state, playerColor), \
                           applyHeuristicDiagonalDownUp(state, playerColor), \
                           applyHeuristicDiagonalUpDown(state, playerColor)
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
            horizontalAndVerticalHelper(bubble, state, playerColor)
            val += horizontalAndVerticalHelper()
    return val


def applyHeuristicVertically(state, playerColor):
    val = 0
    for column in range(0, 7):
        for row in range(0, 3):
            bubble = Bubble(row, column)
            horizontalAndVerticalHelper(bubble, state, playerColor)
            val += horizontalAndVerticalHelper()
    return val


def horizontalAndVerticalHelper(bubble, state, playerColor):
    for i in range(0, 4):
        bubble.values.append(state.matrix[bubble.row][bubble.column])
    return evaluateBubbles(bubble.values, playerColor)

def applyHeuristicDiagonalDownUp(state, playerColor):
    val = 0
    for row in range(0, 3):
        bubble = Bubble(row, 0)
        while bubble.rowStart < 2 and bubble.column < 3:
            val += getValAndIncrementBubblePosition(bubble, state, playerColor, True)
    for column in range(0, 4):
        bubble = Bubble(0, column)
        while bubble.row < 2 and bubble.column < 3:
            val += getValAndIncrementBubblePosition(bubble, state, playerColor, True)
    return val


def applyHeuristicDiagonalUpDown(state, playerColor):
    val = 0
    for row in range(3, 6):
        bubble = Bubble(row, 0)
        while bubble.row > 0 and bubble.column < 3:
            val += getValAndIncrementBubblePosition(bubble, state, playerColor, False)
    for column in range(0, 4):
        bubble = Bubble(column, 6)
        while bubble.row > 0 and bubble.column < 3:
            val += getValAndIncrementBubblePosition(bubble, state, playerColor, False)
    return val


def getValAndIncrementBubblePosition(bubble, state, color, isDownUp):
    for i in range(0, 4):
        columnVal = bubble.column + 1
        if not isDownUp:
            columnVal = bubble.column - 1
        bubble.values.append(state.matrix[bubble.row + i][columnVal])
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
                return 0
            else:
                colorCount += 1
                colorEncountered = color
    if colorEncountered == "white":
        return 1
    else:
        val = 2 ** colorCount
        if colorEncountered is not playerColor:
            val = -val
        return val
