import pandas as pd
a = 'd:/pandas/'
b = pd.read_excel(a)
b = b.pipe(pd.DataFrame.groupby,'class').sum() #pipe()函数用于链式简化
print(b)