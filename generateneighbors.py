from numbertocoordinate import *
from coordinatetonumber import *

# LandCell_List = [1, 5, 6, 13, 14, 16]

# for l in LandCell_List:


def GenerateNeighbors(t1, m, n):
    neighbors = []
    # print(NumberToCoordinate(l, 5, 5))
    # call distance program and check if = 1, if so, add to Island
    r, c = NumberToCoordinate(t1, m, n)
    # print(x)
    # print(y)
    neighbors.append(CoordinateToNumber(r, c-1, m, n))
    neighbors.append(CoordinateToNumber(r-1, c, m, n))
    neighbors.append(CoordinateToNumber(r, c+1, m, n))
    neighbors.append(CoordinateToNumber(r+1, c, m, n))

    return(neighbors)


print(GenerateNeighbors(6, 5, 5))
