"""
字典：
通过key找到其value
字典中的元素是一个个的键值对  不可以重复，不可以使用下标，只能用key来
"""
my_dict1 = {"xiaohong": 99, "xiaoming": 88, "xiaofang": 93}

my_dict2 = {}  # 空字典

score = my_dict1["xiaohong"] # 用key来查找

print(score) # 99

score_dict = {
    "xiaohong":{
        "a":12,
        "b":323,
        "c":22
    },
    "xiaoming":{
        "a":123,
        "b":56,
        "c":225
    },
    "xiaofang":{
        "a":7,
        "b":741,
        "c":98
    }
}
s1 = score_dict["xiaohong"]["c"]
print(s1)  # 22