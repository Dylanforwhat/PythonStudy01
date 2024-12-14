"""
while循环可以定义循环条件
for循环不可以定义循环条件，只能一个一个取

while循环可以做无限循环
for理论上不可以无限循环

while适用于任何场景
for适用于简单或固定次数的循环
"""
def list_while_function():
    my_list = ["a","heima","python"]
    index = 0
    while index < len(my_list):
        x = my_list[index]
        print(f"列表元素为{x}")
        index += 1
list_while_function()

def list_for_function():
    my_list = ["a", "1234", "python"]
    for element in my_list:
        print(f"列表元素为{element}")

list_for_function()