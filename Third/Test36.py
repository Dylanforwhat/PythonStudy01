import pandas as pd

def zhangjia(x):
    return x + 3

a = 'd:/pandas/计算.xlsx'
b = pd.read_excel(a,index_col='序号')
# b['销售金额'] = b['单价'] * b['销售数量']
# print(b)

# for i in range(1,3):
#     b['销售金额'].at[i] = b['单价'].at[i] * b['销售数量'].at[i]
# print(b)

b['单价'] = b['单价'].apply(zhangjia)
print(b)