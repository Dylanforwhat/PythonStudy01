import pandas as pd
years = [1992,1983,1922,1932,1973,1993,1995,1999]  # pandas 分箱比直接sql简单很多
boxs = [1900,1950,2000]
box_names = ['50qian','50hou']
a = pd.cut(years,boxs,labels = box_names)
# a = pd.cut(years,boxs,labels = False) # labels false 之后就返回箱子的序号了，不然默认返回箱子的名字

print(a)
print(pd.value_counts(a))

