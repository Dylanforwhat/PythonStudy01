"""
内置方法（魔术方法）
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__魔术方法
    def __str__(self):
        return f"Studetn类对象，name:{self.name},age:{self.age}"

    # __lt__ 魔术方法
    def __lt__(self, other):
        return self.age < other.age  # 主要是指示在哪里比较

    # __le__ 魔术方法
    def __le__(self, other):
        return self.age <= other.age

    # __eq__ 魔术方法（相等判断）
    def __eq__(self, other):
        return self.age == other.age


stu = Student("xiaohong", 18)
print(stu)
print(str(stu))

stu01 = Student("xiaoA", 30)
stu02 = Student("xiaoB", 100)
print(stu01 < stu02)
print(stu01 > stu02)

stu03 = Student("xiaoC", 30)
print(stu01 <= stu03)

print(stu01 == stu03)
"""
__lt__
自定义比较大小
返回True或者False
"""
