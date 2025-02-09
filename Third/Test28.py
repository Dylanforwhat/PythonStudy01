import pandas as pd
a = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns = ['a','b','c'])
print(a)
print('-'*40)
print(a['b'][0])
print('-'*40)
print(a.iloc[0][2])
print('-'*40)
print(a[['a','b']])