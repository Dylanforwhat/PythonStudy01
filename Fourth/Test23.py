import re
a = '8sV73D1G8E3249'
r = re.match('\d',a)
print(r)
print(r.group())

b = 'life is short,i use python'
r01 = re.findall('life(.*)python',b)
print(r01)

c = '123abc456'
r02 = re.search('([0-9]*)([a-z]*)([0-9]*)',c)
print(r02.group(2))
print(r02.group(3))

