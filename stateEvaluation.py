def evaluateState(state, playerColor):
    totalHeuristicValue = 0
    totalHeuristicValue += applyHeuristicHorizontally(state, playerColor), \
        applyHeuristicVertically(state, playerColor), \
        applyHeuristicDiagonalDownUp(state, playerColor), \
        applyHeuristicDiagonalUpDown(state, playerColor)
    return totalHeuristicValue


def applyHeuristicHorizontally(state, playerColor):
    val = 0
    for row in range(0, 6):
        for startPosition in range(0, 4):
            bubble = []
            for i in range(0, 4):
                bubble.append(state.matrix[row][startPosition + i])
            val += evaluateBubbles(bubble, playerColor)
    return val


def applyHeuristicVertically(state, playerColor):
    val = 0
    for column in range(0, 7):
        for startPosition in range(0, 3):
            bubble = []
            for i in range(0, 4):
                bubble.append(state.matrix[startPosition + i][column])
            val += evaluateBubbles(bubble, playerColor)
    return val


def applyHeuristicDiagonalDownUp(state, playerColor):
    val = 0
    for row in range(0, 3):
        column = 0
        rowStart = row
        while column < 3 and rowStart < 2:
            bubble = []
            for i in range(0, 4):
                bubble.append(state.matrix[rowStart + i][column + i])
            val += evaluateBubbles(bubble, playerColor)
            column += 1
            rowStart += 1
    for column in range(0, 4):
        row = 0
        columnStart = column
        while columnStart < 3 and row < 2:
            bubble = []
            for i in range(0, 4):
                bubble.append(state.matrix[row + i][columnStart + i])
                val += evaluateBubbles(bubble, playerColor)
                columnStart += 1
                row += 1
    return val


def applyHeuristicDiagonalUpDown(state, playerColor):
    val = 0
    for row in range(3, 6):
        rowStart = row
        column = 0
        while rowStart > 0 and column < 3:
            bubble = []
            for i in range(0, 4):
                bubble.append(state.matrix[column + i][rowStart - i])
                val += evaluateBubbles(bubble, playerColor)
                column += 1
                rowStart -= 1
    for column in range(0, 4):
        columnStart = column
        row = 6
        while columnStart < 3 and row > 0:
            bubble = []
            for i in range(0, 4):
                bubble.append(state.matrix[columnStart + i][row - i])
                val += evaluateBubbles(bubble, playerColor)
                columnStart += 1
                row -= 1
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
