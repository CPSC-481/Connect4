from naryTree import State


def minimax(stateTree):
    isMax = stateTree.leafsMinOrMax is "MAX"
    currentLevelNodes = stateTree.leafs[:]
    while currentLevelNodes[0].parent is not stateTree.root:
        currentLevelNodes = getNextMinimaxLayer(currentLevelNodes, isMax)
        isMax = not isMax
    bestState = None
    for node in currentLevelNodes:
        bestState = getMaxOrMinState(bestState, node, isMax)
    return bestState


def getNextMinimaxLayer(currentLevelNodes, isMax):
    newNodeList = []
    for index, node in enumerate(currentLevelNodes):
        if not newNodeList or newNodeList[-1].parent is not node.parent:
            newNodeList.append(node)
        elif newNodeList[-1].parent is node.parent:
            newNodeList[-1] = testIfNextNextNodeBetter(node, newNodeList[-1], isMax)
    return newNodeList


def testIfNextNextNodeBetter(newNode, oldNode, isMax):
    if not isMax:
        if oldNode.value > newNode.value:
            return newNode
    elif isMax:
        if oldNode.value < newNode.value:
            return newNode
    return oldNode


def getMaxOrMinState(bestState, testState, isMax=True):
    if not bestState:
        bestState = getInfiniteState(isMax)
    isGreaterValue = bestState <= testState
    if isGreaterValue:
        if isMax:
            return testState
        return bestState
    if isMax:
        return bestState
    return testState


def getInfiniteState(isMax):
    infiniteState = State(None, None, None)
    infiniteState.value = float("-inf")
    if not isMax:
        infiniteState.value = float("inf")
    return infiniteState
