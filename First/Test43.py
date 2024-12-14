import time

f = open("d:/test.txt", "r", encoding="UTF-8")
print(type(f))

# read
# print(f.read())
# print(f.read(10)) # 无内容 ，read()方法有连续性

# lines = f.readlines() # readlines 返回列表list
# print(lines)

# line1 = f.readline() # read 单独一行
# line2 = f.readline()
# line3 = f.readline()
# print(line1)
# print(line2)
# print(line3)

# for line in f:
#     print(line)
#
# f.close()  # 解除文件的占用

# with open
with open("d:/test.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(line)

time.sleep(5000000)



