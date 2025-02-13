import pandas as pd
import datetime as dt
a = 'd:/pandas/xxx.xlsx'
b = pd.read_excel(a,skiprows = 8,usecols='F:I',dtype={'序号':str,'性别':str,'日期':str})
c = dt.date(2025,2,13)
for i in b.index:
    b['序号'].at[i] = i + 1
    b['性别'].at[i] = 'male' if i%2 == 0 else 'female'
    b['日期'].at[i] = c + dt.timedelta(days = i)
