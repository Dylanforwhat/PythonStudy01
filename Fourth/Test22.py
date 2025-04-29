import re
a = 'C52730A52730D52383'
def sub01(x):
    group01 = x.group()
    if int(group01) >= 5 :
        return '9'
    else:
        return '0'
r = re.sub('\d',sub01,a)
print(r)