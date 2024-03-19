import pandas as pd

# 파일로드
mydata = pd.read_csv('./python_total/mydata.csv', index_col=0)

print(mydata)