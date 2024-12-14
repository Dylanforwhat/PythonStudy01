"""
本代码演示了：
各类字面量的写法
"""
# 写一个整数字面量
111
# 写一个浮点字面量
13.14
# 写一个字符串字面量
"black horse！"

# 定义一个变量，记录钱包余额
money= 100
# 通过print语句，输出变量记录的内容
print("钱包还有余额：" , money)
# 买了一个冰淇凌，花费10元
money = money -10
print("买了冰淇凌，还剩余", money)

# 使用type()验证数据类型
print(type("love you "))
name = "qqqqq"
nametype = type(name)
print(nametype)