import pandas as pd
a = pd.Series([0,1,2],index = ['a','b','c'])
print(a)
b = pd.Series([3,4],index = ['d','e'])
print('*'*30)
print(b)
print('*'*30)
c = pd.concat([a,b])
print(c)