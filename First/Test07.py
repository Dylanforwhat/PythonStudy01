# 占位拼接
name = "black horse"
message = "learn IT come:%s" % name  # 用%号进行占位
print(message)

# 通过占位的形式，完成数字和字符串的拼接
class_num = 57
avg_salary = 17222
message = "Python beijing:%s,salary:%s" % (class_num,avg_salary)
print(message)

# 快速格式化+占位 f"{ }"
name = "qiuweili"
set_up_year = 1988
stock_price = 36
print(f"我是{name},我出生于{set_up_year},我今年{stock_price}")