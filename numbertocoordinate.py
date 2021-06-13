import numpy as np
from coordinatetonumber import *


def NumberToCoordinate(t, m, n):
    arr = [i for i in range(m*n)]
    arr_2d = np.reshape(arr, (m, n))
    for i in range((arr_2d.shape[0])):
        for j in range((arr_2d.shape[1])):
            if arr_2d[i, j] == t:
                return(i, j)
                break

######## TESTING the METHOD ########################

# a = NumberToCoordinate(23, 10, 10)
# print(a)
# print(NumberToCoordinate(CoordinateToNumber(2, 3, 10, 10), 10, 10))
