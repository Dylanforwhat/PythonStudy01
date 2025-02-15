import pandas as pd
a = 'd:/pandas/去重.xlsx'
b = pd.read_excel(a,index_col='序号')
# print(b['姓名'].unique())
print(b['姓名'].value_counts())

print(b.drop_duplicates(subset = ['姓名'],keep = 'first'))

print(b.drop_duplicates(subset = ['姓名'],keep = False))

print(b[b.duplicated(subset = '姓名')]) # 选取重复数据