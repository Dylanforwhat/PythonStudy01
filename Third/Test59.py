import pandas as pd
a = 'd:/pandas/data01.xlsx'
b = pd.read_excel(a,index_col= False)
# c = {'男':'先生','女':'女士'}
# b['称呼'] = b['性别'].map(c)  # map就是映射  replace 分情况使用

# def 替换(x):
#     称呼 = '先生' if x == '男' else '女'
#     return 称呼
#
# def modify01(x,change):
#     return x + change
# b['语文'] = b['语文'].apply(modify01,args = (-5,))
#
# b['称呼'] = b['性别'].map(替换)


#d = b['语文'].apply(sum,axis = 0)
def BMI(b):
    height = b['身高']
    weight = b['体重']
    BMI = height/weight **2
    return BMI
b['BMI'] = b.apply(BMI,axis = 1)
print(b)