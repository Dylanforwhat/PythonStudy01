import numpy as np
a = np.random.permutation(10)
print(a)
print('-'*40)
b = np.arange(9).reshape((3,3))
print(b)
print('-'*40)
c = np.random.permutation(b)
print(c)