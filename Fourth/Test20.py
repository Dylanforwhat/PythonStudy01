import re
tel = '13811115888'
r = re.findall('^\d{11}$',tel)
print(r)


a = "abcabcabcxyzzabcxyabc"
r1 = re.findall('(abcabc)',a)
print(r1)

b = 'abcFBIabcCIAabc'
r2 = re.findall('fbi',b,re.I)
print(r2)

r3 = re.findall('fbi.{1}',b,re.I)
print(r3)