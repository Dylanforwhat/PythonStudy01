"""
构造方法:__init__
"""
class Student:
    # name = None
    # age = None
    # tel = None 可以不写

    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("create a class object!") # 构造方法自动执行

stu01 = Student("xiaohong",18,"1862775455")
print(stu01.tel)
print(stu01.name)







