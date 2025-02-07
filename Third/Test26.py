# dataframe 二维数据，多行多列，整个表格
# series 一维数据，一行或者一列
import pandas as pd
a = pd.Series(['xiaohong','male','20','2000-10-07'])
print(a)
print(a.index)
print('-'*40)
b = {'name':'xiaofang','gender':'male','age':'20','birth':'2002-04-12'}
c = pd.Series(b)
print(c)
print(c.index)
print(c['name'])
print(c[['name','gender']])  # 同时查询两个key得值，注意，没有['name','gender']这个key值，你得给一个列表，如左所示
