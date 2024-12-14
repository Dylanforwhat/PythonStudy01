"""
多态

多种状态，完成某一个动作，不同对象得到不同的状态

多态作用在继承基础之上

以父类作定义声明
以之类作实际工作
用以获得同一行为，不同状态

多态的优点：
*父类用来确定有哪些方法
*具体的方法实现由子类自行决定

以上的写法就是抽象类

还有抽象方法的类被称为抽象类

方法体是空实现（pass）称之为抽象方法

抽象类配合多态，完成：
1、抽象的父类设计（设计标准）
2、具体的子类实现（实现标准）

抽象类 要求子类必须复写父类的方法

"""

class Animal:
     def speak(self):
         pass

class Dog(Animal):
    def speak(self):
        print("wangwangwang!")

class Cat(Animal):
    def speak(self):
        print("ニャー")

def makenoise(animal:Animal):
    animal.speak()

dog = Dog()
cat = Cat()

makenoise(dog)
makenoise(cat)