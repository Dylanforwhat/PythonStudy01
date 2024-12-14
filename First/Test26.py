"""
体验给、函数的开发及使用
需求：统计字符串的长度，不使用内置函数len（）

"""

str1 = "itheima"
str2 = "itcast"
str3 = "python"

count = 0
for i in str1:
    count += 1
print(f"字符串{str1}的长度是{count}")

count = 0
for i in str2:
    count += 1
print(f"字符串{str2}的长度是{count}")

#  使用函数，优化代码,封装
def mylen(data):
    count = 0
    for i in data:
        count +=1
    print(f"字符串{data}的长度是{count}")

mylen(str1)
