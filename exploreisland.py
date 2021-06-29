from numbertocoordinate import *
from coordinatetonumber import *
from readfile import *
from generateneighbors import *


def ExploreIsland(t1, n, m):
    cells_in_island = []
    coord = NumberToCoordinate(t1, m, n)
    if coord in LandCoordinates('test.txt'):
        cells_in_island.append(t1)
        neighbors = GenerateNeighbors(t1, m, n)
        for neighbor in neighbors:
            cells_in_island = cells_in_island + ExploreIsland(neighbor, m, n)
    return cells_in_island


# ExploreIsland(2, 5, 5)
