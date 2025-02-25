import pandas as pd
a = 'd:/pandas/转换.xlsx'
b = pd.read_excel(a)
b = pd.DataFrame(b.values.T,index = b.columns,columns = b.index)
print(b)