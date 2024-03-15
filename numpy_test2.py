import numpy as np

def printinfo(arr):
    print(arr)

origin_arr = np.arange(12)
printinfo(origin_arr)

reshape_arr = np.reshape(origin_arr, (4, 3))
printinfo(reshape_arr)

reshape_arr = reshape_arr.reshape(-1, 2)
printinfo(reshape_arr)