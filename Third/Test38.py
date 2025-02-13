import pandas as pd
a = 'd:/pandas/计算.xlsx'
b = pd.read_excel(a,index_col='序号')
b['降价'] = b['商品名称'].apply(lambda x:-4 if x !='苹果' else 0)
b['最终价格'] = (b['单价'] + b['降价']) * b['销售数量']
print(b)