import pandas as pd
a = 'd:/pandas/xx'
b = pd.read_excel(a)
c = b.groupby(['城市','区'])[['人数','金额']].sum() # 前面是按谁分组，后面是对谁聚合,聚合方式。#承诺不首先使用for循环
print(c)


List1 = ['1季度','1季度','1季度','2季度','2季度']
List2 = ['1月','2月','3月','4月','5月']

A = pd.MultiIndex.from_arrays([List1,List2],names = ['season','month'])
B = pd.DataFrame(数据,columns = A)
C = B.groupby(Level = 'season',axis = 1).sum()