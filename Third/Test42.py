import pandas as pd
a = 'd:/pandas/筛选.xlsx'
b = pd.read_excel(a,index_col='出生日期',parse_dates=['出生日期'])
c = b.sort_values('出生日期')

print(c['1983':'1990'])
print(c.loc['1983':'1990'])

tiaojian = (
    '@b.出生日期.dt.year > 1980 and'
    '@b.出生日期.dt.year < 1990'
    'and 性别 == "男"'

)
print(b.query(tiaojian   ))
