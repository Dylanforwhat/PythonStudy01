import pandas as pd
import numpy as np
arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
a = pd.DataFrame(arr,columns = list('xyz'),index = list('abc'))
print(a.apply(np.square)) # 全表平方根

b = a.apply(lambda m:np.square(m) if m.name == 'x' else m) # 单列平方根
c = a.apply(lambda m:np.square(m) if m.name in ['x','y'] else m) # 多列平方根
d = a.apply(lambda m:np.square(m) if m.name == 'a' else m,axis = 1) # 单行平方根
print(b)
print(c)
print(d)