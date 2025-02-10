import pandas as pd
a = {
    'name':['xiaohong','xiaofang','xiaodiao'],
    'age':[20,80,123],
    'job':['singer','worker','scientist']
}
b = pd.DataFrame(a)
print(b)
print(b.columns)
print('-'*40)
print(b.loc[1])
print('-'*40)
print(b[['name','age']])  # 查询列 直接用列表里面转columns名
print('-'*40)
print(b.loc[0:3]) # 查询row 用loc