"""
use for循环  to do 99乘法表
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i} = {j * i}\t", end='')
    print()
