import pandas as pd
a = pd.DataFrame({'name':['zhangsan','lisi','wangwu','zhangsan','lisi'],'times':range(5)})
b = pd.DataFrame({'age':[10,20]},index = ['zhangsan','lisi'])
print(a)
print(b)
print('-'*40)
c = pd.merge(a,b,left_on = 'name',right_index= True)
print(c)