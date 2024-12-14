"""
Input语句
1、使用input()语句可以从键盘获取输入
2、使用一个变量接收input语句获取的键盘输入数据
"""


name = input("tell me who are you")
print("You are :%s" % name)

num = input("tell me your number")
num = int(num)
print("number:%d" % num)