import pandas as pd
a = 'd:/pandas/xx.xlsx'
b = pd.read_excel(a,sheet_name = 'names')
c = pd.read_excel(a,sheet_name = 'grades')
d = pd.merge(b,c.loc[:,['numbers','total']],how = 'left',on = 'numbers')
