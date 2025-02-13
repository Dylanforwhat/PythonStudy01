import pandas as pd
a = 'd:/pandas/计算.xlsx'
b = pd.read_excel(a,index_col='序号')

b['单价'] = b['单价'].apply(lambda x:x + 3)
print(b)