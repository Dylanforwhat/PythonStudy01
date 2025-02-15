import pandas as pd
a = 'd:/pandas/多层索引.xlsx'
b = pd.read_excel(a,index_col=[0,1])

print   (b)