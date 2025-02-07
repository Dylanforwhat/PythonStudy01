import pandas as pd
a = ['name','gender','age']
b = ['xiaofang','female','29']
c = pd.Series(b,index = a)
print(c)
print(c.index)
print(c.values)