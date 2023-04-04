def createDiamondGridMatrix(long):
    gridMatrix = list()
    pas = 0
    for i in range(long):
        gridMatrix.append([1]*long)
        for j in range(0, long//2 - pas, 1):
            gridMatrix[i][-j-1] = 0
            gridMatrix[i][j] = 0
        if i < (long//2):
            pas += 1
        else:
            pas -= 1
    return gridMatrix
