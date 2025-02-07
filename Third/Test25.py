import pandas as pd
a  = 'd:/pandas/邱伟力.xlsx'
b = pd.read_excel(a,header = None,names = ['No','Name'],index_col ='No')
print(b)
b.to_excel(a)
print(b.sort_index())
print(b.sor_values('name'))
