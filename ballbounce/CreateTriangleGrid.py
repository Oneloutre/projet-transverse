def createTriangleGridMatrix(long):
    gridMatrix = []
    for i in range((long//2) + 1):
        gridMatrix.append([1]*long)
        for j in range((long//2) - i):
            gridMatrix[i][-j-1] = 0
            gridMatrix[i][j] = 0
    return gridMatrix


