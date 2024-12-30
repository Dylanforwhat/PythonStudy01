import numpy as np
def xiangjia(n):
    a = np.arange(1,n+1)**3
    b = np.arange(1,n+1)**2
    return a + b
print(xiangjia(3))
