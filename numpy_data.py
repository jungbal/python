# txt 파일을 numpy를 이용하여 배열로 불러오기
import numpy as np

# txt 파일 불러오기
data = np.loadtxt("../python/data.txt", delimiter = ",", dtype = np.int64)

#처음부터 3행까지, 전체열
print(data[:3, :])

print(data.shape)