"""
字符串的三种定义
单引号定义法
双引号定义法
三引号定义法 支持换行操作
"""

name = '黑马'
name1 = "黑马"
name2 = """
我是
黑马
"""

# 单引号包含双引号
name3 = '"black horse"'
# 使用转义字符\ 解除引号的效用
name4 = "\"black horse\""

# 字符串字面量的拼接

# 字符串字面量和字符串变量的拼接
name5 = "black hores"
tel = 10902322
# print("I'm" + name5 + "my number is" + tel) 整数或者浮点数 没有办法直接跟字符串进行拼接

