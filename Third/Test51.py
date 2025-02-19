import pandas as pd
import os
a =  'd:/pandas/课件025/'
b = pd.DataFrame()  # b 这里是一个新建的一个空的主表，用来放拼接过来的表内容
for names in os.listdir(a):
    c = pd.read_excel(a + names) # 这里这个加号妙啊 # 加上None参数可以读取多所有的sheet
    b = pd.concat([b,c])#

print(b)

b.to_excel('d:/pandas/合并表.xlsx',index = False)