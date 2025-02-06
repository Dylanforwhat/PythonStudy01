import pandas as pd

a = pd.DataFrame({'No':[1,2,3],'name':['xiaohong','xiaoming','xiaohua']})
a = a.set_index('No')
a.to_csv('d:/pandas/邱伟力.csv')

print('创建成功！')