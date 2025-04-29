import re
a = 'abcFBIabcCIAabc'
def sub01(y):
    a = y.group()
    return '$' + a + '$'
r = re.sub('FBI',sub01,a)
print(r)
