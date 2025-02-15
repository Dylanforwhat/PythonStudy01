import pandas as pd
a = "gender == 'male' and socre >= 150"
print(数据.query(a))  # query 支持and

b = "name in ['xiaohong','xiaoming']"
print(数据.query(b))

c = 数据['name'].str.startswith('x')

d = 数据['address'].str.contains('[a-cA-C]+座')

e = "60 <= yuwen <= 100 and gender == 'female' "
print(数据.query(e))
