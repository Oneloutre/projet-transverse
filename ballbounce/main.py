from CreateCircleGrid import returnRayon, createCricleGridMatrix
from CreateDiamondGrid import createDiamondGridMatrix
from CreateTriangleGrid import createTriangleGridMatrix
from displayMatrix import returnDisplayGridMatrixLine

long = int(input('Long'))
gridMatrix = createDiamondGridMatrix(long)
for i in range(long):
    print(returnDisplayGridMatrixLine(gridMatrix, i))
