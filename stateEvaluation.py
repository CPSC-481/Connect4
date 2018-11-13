def evaluateState(state, playerColor):
    totalHeuristicValue = 0
    totalHeuristicValue += applyHeuristicHorizontally(state, playerColor)
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
