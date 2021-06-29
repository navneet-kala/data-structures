from numbertocoordinate import *
from coordinatetonumber import *
from readfile import *
from generateneighbors import *
from exploreisland import *


def FindIslands(LandCell_List):
    Island_List = []
    for l in LandCell_List:
        island = ExploreIsland(l, n, m)
        if len(island) > 0:
            Island_List.append(island)
    return Island_List
