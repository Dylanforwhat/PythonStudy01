"""
文件的写入 write模式
特点 自动新建文件，覆盖原文件内容

"""
import time

f = open("d:/test01.txt","w",encoding = "UTF-8") #

f.write("hello world")
f.flush()
# time.sleep(600000)
f.close() # close 内置flush功能