import numpy as np
a = np.array([3,6,7,9,2,1,8,5,4])
a.sort()
print(a)

b = np.array([[0,12,48],[4,18,14],[7,1,99]])
print(f'{b}')
print('-'*30)
print(np.sort(b)) # 二维数组的sort排序默认是按axis=1 就是按列排序进行的
print('-'*30)
print(np.sort(b,axis = 0))