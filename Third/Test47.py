import pandas as pd

a  = pd.MultiIndex.from_arrays([['a','a','b','b'],[1,2,1,2]],names =['x','y'])
print(a)

b = pd.MultiIndex.from_tuples([('a',1),('a',2),('b',1),('b',2)],names = ['x','y'])
print(b)