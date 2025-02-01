import numpy as np
a = np.arange(1,21).reshape(4,5)
print(a)
b = a[:,3]>5
print(b)
a[: ,3][b] = 520
# a[a[:,3]>5] = 520
print(a)