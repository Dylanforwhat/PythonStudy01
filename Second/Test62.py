"""
演示面向对象封装思想中私有成员的使用
"""
# 定义一个类，内含私有成员变量和私有成员方法

class Phone:
    __current_vol = 0.5
    def __keep_single_core(self):
        print("cpu running single core!")

# phone01 = Phone()
# phone01.__keep_single_core() #类对象无法访问私有方法或私有变量,报错
# print(phone01.__current_vol)
    def call_5g(self): # 类中的其他方法可以访问私有变量或私有方法
        if self.__current_vol >=1:
            print("5g is ready!")
        else:
            self.__keep_single_core()
            print("5g is not available,switch to single core!")

phone = Phone()
phone.call_5g()