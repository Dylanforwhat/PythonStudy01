import re
a = '孙悟空7猪八戒6沙和尚3唐僧6白龙马'
r = re.findall('[0-9]',a)
print(r)

r1 = re.findall('[^0-9]',a)
print(r1)

b = 'xyz,xcz,xfz,xaz,xez'
r3 = re.findall('x[de]z',b) #[]中的是并列或的详细
print(r3)

r4 = re.findall('x[d-f]z',b)
print(r4)

c = 'excel 12314word\n 2345_ppt123dlr'
r5 = re.findall('\d',c)
print(r5)

r7 = re.findall('\D',c)
print(r7)

d = 'excel 12314word\n 2345$$_ppt123dlr'
r8 = re.findall('\w',d)
print(r8)

r9 = re.findall('\W',d)
print(r9 )
