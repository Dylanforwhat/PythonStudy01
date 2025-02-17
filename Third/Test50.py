import pandas as pd
# cat()指定字符连接
print(shuju['name'].str.cat(['jiahouzui']*len(shuju),sep = '/',na_rep = 'wuming'))
# split()  英文原意：分裂。 指定字符进行分割，指定字符被删除
print(shuju['zhuantai'].str.split('xue',expand = True)) # expand 是分列的意思
# partition() 英文愿意：隔断。指定字符前后进行隔断，指定字符存活。
print('BbBbBb'.partition('b'))# 注意！只隔断第一个出现的字符
# get() 获取指定位置的字符   slice() 注意！slice是片的意思，slice后面输入范围
print(shuju['zhuangtai'].str.get(2))
# slice() 切片 注意！slice是片的意思，slice后面输入范围
print(shuju['zhuangtai'].str.slice(0,3,2)) #左闭右开，步长为2
# slice_replace() 切片后替换
print(shuju['zhuangtai'].str.slice(0,3,'money')) # 只替换一次，不支持步长
# join() 每个字符之间用指定字符相连接
print(shuju['zhuangtai'].str.join('502'))
# contains() 判断是否含有，返回布尔
print(shuju['zhuangtai'].str.contains('xue',na = False)) # 如果有NaN,记得使用na转换
# startswith() 判断是否以什么开始，返回布尔
# endswith() 判断是否以什么结尾，返回布尔
# repeat() 重复字符串，填入重复次数
print(shuju['zhuangtai'].str.repeat(3))
# pad() pad英文有‘填塞’之意。每个元素用指定字符填充， fillchar用什么字符填充，数字是填充到几位，side是优先从那边开始补齐
print(shuju['name'].str.pad(5,fillchar = '&',side = 'both'))
# encode decode 编码 解码
print(shuju['name'].str.encode('utf-8').str.decode('utf-8'))
# strip() 从两边去除  lstrip() 左边去除  rstrip()右边去除
# get_dummies() 字符分割,结果是除了该字符以外，其他本行因该字符被分割的所有字符的出现次数
print(shuju['name'].str.get_dummies('ju'))
# maketrans() 指定字符转换，里面可以写字典
str.maketrans({'邱':'qiu','维尼':'weili'})
# find() 查找指定字符第一次出现的位置 rfind()从右边开始找，找不到-1
print(shuju['date']).astype('str').str.find('-')# 对日期的操作要先使用astype进行转换操作，这里.str.不是转换，而是调用str方法
