import pandas as pd
a = 'd:/pandas/筛选.xlsx'
b = pd.read_excel(a,index_col='出生日期',parse_dates=['出生日期'])
c = b[b['出生日期']>pd.to_datetime('1988-10-01')]
print(c.head())

