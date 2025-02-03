import numpy as np
a = np.array([1,2,3,4,3,5,3,6])
print(np.sum(a))
print('-'*30)
print(np.cumsum(a))   #累加
print('-'*30)
print(np.cumprod(a))  #累乘
print('-'*30)
print(np.argmax(a))  # 最大值下标