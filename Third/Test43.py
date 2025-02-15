import pandas as pd
a = 'd:/pandas/xx.xlsx'
b = pd.read_excel(a,index_col='序号')

print(b.isnull()) # 查看空值
print(b.notnull()) # 查看非空值
print(b.dropna(axis = 1,how = 'all')) # all的意思是全空才drop
print(b.dropna(axis = 1,thresh = 2)) # 至少有2个非空值，不然drop该行
print(b.dropna(subset= ['语文','数学']))

print(b.fillna(520)) # 所有非空值填充520
print(b.fillna({'语文':100,'数学':80})) # 不同列进行不同填充，效率高于excel

print(b.fillna(method='ffill')) # 用该列空值前一个值，填充
print(b.fillna(method = 'bfill',limit=2))# 用该列空值后的一个值填充，limit限制填充数量