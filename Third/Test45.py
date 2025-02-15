import pandas as pd
a = 'd:/pandas/计算2.xlsx'
b = pd.read_excel(a)

c = b['1店']+b['2店']  # NaN加任何值都为Nan
d = b['1店'].fillna(0)+b['2店'].fillna(0) # 把空值替换为0 可以计算
print(c)
print(d)