import pandas as pd
import os
a = 'd:/pandas/hebing.xlsx'
b = pd.read_excel(a,None) # None 这里是未指定sheet名字，意为所有的sheet
c = pd.DataFrame() # 新建一个空的主表

d = list(b.keys()) # excel 的keys就是表头的意思 把表头都拿出来做个list
for columns in d:
    e = b[columns] # 按excel的表头循环，提出每列数据丢进空的dataframe中
    c = pd.concat([c,e])
print(c)


