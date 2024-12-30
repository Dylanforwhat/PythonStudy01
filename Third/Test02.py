import numpy as np

from my_utils.file_util import print_file_info

b = np.array(range(1,6))
print(b)

c = np.arange(1,6)
print(c)

e = np.array(range(1,10),dtype = float)
print(e)

print(type(b))

print(c.dtype)
print(c.shape)

f = np.arange(1,20,2)
print(f)

g = np.ones(4)
print(g)

h = np.ones((2,3))
print(h)

l = np.full((3,3),520)
print(l)