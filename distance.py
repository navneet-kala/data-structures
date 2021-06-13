from numbertocoordinate import *
from readfile import *


def Distance(t1, t2):
    c1 = NumberToCoordinate(t1, m, n)
    c2 = NumberToCoordinate(t2, m, n)
    # print(c1)
    # print(c2)
    return(abs(c1[0]-c2[0])+abs(c1[1]-c2[1])-1)


######## TESTING the METHOD ########################
# ALL THIS CODE CAN BE IN SEPARATE DRIVER OR MAIN PY FILE

coordinates = LandCoordinates('navneet-kala.txt')
# Loop to get multiple test cases and their corresponding shapes, the shape is needed to call NumberToCoordinate method
number_cases = coordinates['total-testcases'][0][0]
for k in range(1, int(number_cases)+1):
    m = coordinates[f'shape-testcase-{k}'][0][0]
    n = coordinates[f'shape-testcase-{k}'][0][1]
dist = Distance(13, 33)
print(dist)
