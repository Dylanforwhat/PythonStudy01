my_str = "itheima and itcast"

a = my_str[2]

b = my_str[-2]

print(a, b)
"""
这里replace得到一个新的字符串
"""
new_my_str = my_str.replace("it", "internet")
print(new_my_str)

my_str_list = my_str.split(" ")
print(my_str_list)
