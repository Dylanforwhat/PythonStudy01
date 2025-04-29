import re
a = 'ExcelVBA 12314Word34353PPT12Lr'
r1 = re.findall('[a-zA-Z]{3,5}',a) # 大括号表示要提取的单词长度
print(r1)
# python默认贪婪模式

b = 'exce0excell3excelabc3'
r2 = re.findall('excel*',b)
print(r2)

r3 = re.findall('excel+',b)
print(r3)
