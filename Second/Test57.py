# 设计一个类，（设计一个登记表）
class Student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None   # Java中是  int age  ， String name

# 创建一个对象
stu01 = Student()
# 对对象进行赋值
stu01.name = "xiaohong"
stu01.gender = "man"
stu01.nationality = "China"
stu01.native_place = "shadong"
stu01.age = 31

print(stu01.name,stu01.age)