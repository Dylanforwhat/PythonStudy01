# 数组的转置换轴  除了 reshape()方法之外，还有
# 1、行列装置 transpose

import numpy as np
a = np.arange(24).reshape((4,6))
print(a)
print('-'*40)
print(a.transpose())

# 2、轴装置 swapaxes()
print('-'*40)
print(a.swapaxes(1,0))