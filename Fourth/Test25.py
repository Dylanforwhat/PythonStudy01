import re
from re import findall

#元字符匹配功能
s = 'itheima @@pythontcast3'
re01 = findall(r'\d',s)  #前面这个r表示转义字符无效，不然报错，当时可以出结果。
print(re01)

re02 = findall(r'\W',s)
print(re02)

re03 = findall('[a-zA-Z]',s)
print(re03)

re04 = findall('[a-zA-Z]{6,8}',s)
print(re04)