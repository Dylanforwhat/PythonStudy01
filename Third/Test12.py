import random
import numpy as np
random.seed(2000)
print(random.random())
print(random.random())
print(random.random())
print('-'*40)
b= np.random.rand(3)
c = np.random.rand(3,4)
d = np.random.rand(3,4,5)
print(b)
print(c)
print(d)
print('-'*40)
e = np.random.randint(1,20,size= (3,4))
print(e)
