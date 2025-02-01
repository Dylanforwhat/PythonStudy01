import numpy as np
a = np.arange(36).reshape(9,4)
print(a)
print('-'*30)
print(a[[4,3,0,6]])
print('-'*30)
print(a[[0,5,7],[0,2,1]])
print('-'*30)
print()