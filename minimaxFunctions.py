from naryTree import swapTurnColor
from stateEvaluation import evaluateState
from naryTree import State


def minimax(stateTree, color):
    isMax = getLeafMinOrMax(stateTree.isMax, stateTree.plyLevel)
    currentLevelNodes = stateTree.leafs[:]
    while currentLevelNodes[0].parent is not stateTree.root:
        for state in currentLevelNodes:
            state.value = evaluateState(state, color)
        currentLevelNodes = getNextMinimaxLayer(currentLevelNodes, isMax)
        isMax = not isMax
        color = swapTurnColor(color)
    bestState = None
    for index, node in enumerate(currentLevelNodes):
        if getMaxOrMinState(bestState, node, isMax):
            bestState = node
            bestChoice = index
    return bestChoice


def getNextMinimaxLayer(currentLevelNodes, isMax):
    newNodeList = []
    for index, node in enumerate(currentLevelNodes):
        if not newNodeList or newNodeList[-1].parent is not node.parent:
            newNodeList.append(node)
        elif newNodeList[-1].parent is node.parent:
            newNodeList[-1] = testIfNextNextNodeBetter(node, newNodeList[-1], isMax)
    for index, node in enumerate(newNodeList):
        node.parent.value = node.value
        newNodeList[index] = node.parent
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
    isGreaterValue = bestState.value <= testState.value
    if isGreaterValue:
        if isMax:
            return True
        return False
    if isMax:
        return False
    return True


def getInfiniteState(isMax):
    infiniteState = State()
    infiniteState.value = float("-inf")
    if not isMax:
        infiniteState.value = float("inf")
    return infiniteState


def getLeafMinOrMax(isMax, plyLevel):
    if plyLevel % 2 is 0:
        return isMax
    return not isMax

