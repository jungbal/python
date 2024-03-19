import pandas as pd

# dictionary 생성
data = {'ID' : ['A1', 'B1', 'C1', 'D1', 'E1'],
        'X1' : [1, 2, 3, 4, 5],
        'X2' : [3.0, 4.5, 3.2, 4.0, 3.5]}

print(data)

# dataframe 형식으로 변환(index로 라벨 추가)
mydata = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e'])

print(mydata)