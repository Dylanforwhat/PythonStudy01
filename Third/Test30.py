import pandas as pd
import numpy as np
a = pd.DataFrame({'name':['xiaohong','xiaofang','xiaodiao','xiaofang','xiaohong','xiaohong'],'rounds':np.arange(6)})
b = pd.DataFrame({'name':['xiaojj','xiaodiao','xiaofang'],'rounds':[1,2,3]})
c = pd.merge(a,b)
print(c)
print('-'*40)
print(pd.merge(a,b,on = 'name', how = 'left')) # on 是两个表都有字段