import numpy as np

data = np.loadtxt("../python/data.txt", delimiter = "::", dtype = np.int64)

print(data[:5, :])
print(data.shape)