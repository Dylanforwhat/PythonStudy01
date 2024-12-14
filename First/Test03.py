# 将数字转换为字符串
Str1 = str(11)
print(type(Str1),Str1)
# 将字符串转换成数字
# 注意：想要把字符串都转换成数字，必须要求字符串内的内容都是数字
num1 = int("11")
print(type(num1),num1)

# 整数转浮点数
float_num1 = float(11)
print(type(float_num1),float_num1)
# 浮点数转整数 (注意：会丢失精度)
int_num2 = int(11.345)
print(type(int_num2),int_num2) # 结果为11