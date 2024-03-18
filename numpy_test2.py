# numpy를 이용한 다차원 배열 생성
import numpy as np

def printinfo(arr):
    print(arr)

origin_arr = np.arange(12)
printinfo(origin_arr)

# 3개의 데이터씩 4행
reshape_arr = np.reshape(origin_arr, (4, 3))
printinfo(reshape_arr)

# 2개의 데이터씩 6행
reshape_arr = reshape_arr.reshape(-1, 2)
printinfo(reshape_arr)