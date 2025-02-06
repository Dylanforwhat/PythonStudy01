# 布尔索引  等于把数组0和1化
import numpy as np
a = np.arange(10)
print(a)
b = a > 5
print(b)
print(a[a>5])

# 自增量操作
a[a >5] += 520
print(a)

