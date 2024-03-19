import pandas as pd

data = {'ID' : ['A1', 'B1', 'C1', 'D1', 'E1'],
        'X1' : [1, 2, 3, 4, 5],
        'X2' : [3.0, 4.5, 3.2, 4.0, 3.5]}

print(data)

# dataframe 형식으로 변환(index로 라벨 추가)
mydata = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e'])

print(mydata)

# x1변수를 선택해 상위 행 보기
mydata['X1'].head()

# x1변수의 두번째 행부터 4번째 행까지 보기
mydata[1:5]['X1']

mydata.rename(columns={'X1':'item1'}, inplace=True)

print(mydata)