"""
类的定义和使用
class 类名称：
     1、类的属性：定义在类中的变量（成员变量）
     2、类的方法：定义在类中的函数（成员方法）
创建类对象的语法：
对象 = 类名称（）

"""

class Student:
    name = None
    age = None
    def say_hi(self):
        print(f"hello,I`m {self.name}") # self关键字类似this
    # 在成员方法中访问class中定义的成员变量用"self"

    def say_hi2(self,msg):
        print(f"hello,Im {self.name}, {msg}")

stu01 = Student()
stu01.name = "xiaogang"
stu01.say_hi()

stu02 = Student()
stu02.name = "xiaohong"
stu02.say_hi()

stu03 = Student()
stu03.name = "xiaohuang"
stu03.say_hi2("and going to sing")