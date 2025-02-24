import pandas as pd
a = 'd:/pandas/data01.xlsx'
b = pd.read_excel(a)

c = b.applymap(lambda x:"%.3f" % x)

