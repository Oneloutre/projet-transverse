from math import sqrt


def returnRayon(long):
    return long//2+1


def createCricleGridMatrix(rayon):
    gridMatrix = []
    for i in range(-(rayon-1), rayon, 1):
        temp = []
        for j in range(-(rayon-1), rayon, 1):
            if sqrt((i**2) + j**2) <= rayon:
                temp.append(1)
            else:
                temp.append(0)
        gridMatrix.append(temp)
    return gridMatrix
