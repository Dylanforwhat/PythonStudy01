my_dict = {"xiaohong": 99, "xiaoming": 88, "xiaofang": 93}

my_dict["xiaoli"] = 66
print(my_dict)

my_dict.pop("xiaoming")
print(my_dict)

my_dict.clear()
print(my_dict)

my_dict = {"xiaohong": 99, "xiaoming": 88, "xiaofang": 93}
keys1= my_dict.keys()
print(keys1)

# 用keys进行for循环遍历
for key in keys1:
    print(key)
    print(my_dict[key])
# 直接for循环遍历
for key in my_dict:
    print(key)
    print(my_dict[key])
