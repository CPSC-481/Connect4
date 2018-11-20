

class State:
    def __init__(self, parent, matrix, columnCounts):
        self.parent = parent
        self.children = []                              # an empty list
        self.matrix = copyMatrix(matrix)                # a matrix
        self.columnCounts = columnCounts[:]             # a counter
        self.value = None                               # none is null
        self.alphaBeta = {"alpha": None, "beta": None}  # values for alpha and beta. none equivalent to null


class StateTree:
    def __init__(self, root, plyLevel, initialTurnColor):
        self.root = root
        self.leafs = []
        self.plyLevel = plyLevel
        self.generateStatesToPlyLevel(root, 1, initialTurnColor)
        self.isMax = True

    def generateStatesToPlyLevel(self, state, ply, color):
        if ply <= self.plyLevel:
            for index, column in enumerate(state.columnCounts):
                if column < 5:                                                   # columns are indexed 0 1 2 3 4 5
                    newState = State(state, state.matrix, state.columnCounts)
                    newState.columnCounts[index] += 1
                    newState.matrix[column][index] = color
                    state.children.append(newState)
                    self.isMax = not self.isMax
                    self.generateStatesToPlyLevel(newState, ply + 1, swapTurnColor(color))
        else:
            self.leafs.append(state)

def swapTurnColor(color):
    if color is "yellow":
        color = "red"
    else:
        color = "yellow"
    return color

def copyMatrix(matrix):
    newMatrix = []
    for row in matrix:
        newMatrix.append(row[:])
    return newMatrix
