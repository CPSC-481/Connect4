class State:
    def __init__(self, parent, matrix, columnCounts):
        self.parent = parent
        self.children = []                              # an empty list
        self.matrix = matrix                            # a matrix
        self.columnCounts = columnCounts                # a counter
        self.value = None                               # none is null
        self.alphaBeta = {"alpha": None, "beta": None}  # values for alpha and beta. none equivalent to null


class StateTree:
    def __init__(self, root, plyLevel, initialTurnColor):
        self.root = root
        self.leafs = []
        self.plyLevel = plyLevel
        self.generateStatesToPlyLevel(root, 1, initialTurnColor)

    def generateStatesToPlyLevel(self, state, ply, color):
        if ply is not self.plyLevel:
            for index, column in enumerate(state.columnCounts):
                if column is not 6:                             # columns are indexed 0 1 2 3 4 5
                    newMatrix = state.matrix
                    newMatrix[index][column + 1] = self.currentTurn
                    newColumnCount = state.columnCounts
                    newColumnCount[index] += 1
                    newState = State(state, newMatrix, newColumnCount)
                    state.children.append(newState)
                    self.generateStatesToPlyLevel(state, ply + 1, self.swapTurnColor(color))
        else:
            self.leafs.append(state)

    def swapTurnColor(self, color):
        if color is "yellow":
            color = "red"
        else:
            color = "yellow"
        return color