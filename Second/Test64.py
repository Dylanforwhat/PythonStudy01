"""
复写
"""
class Phone:
    IMEI = None
    producer = "SB"

    def call_5g(self):
        print("5g is ongoing!")

class MyPhone(Phone):
    producer = "BigSB" # 直接同名重写

    def call_5g(self):
        print("cpu change to single core!")
        print("5g is ongoing!")

phone = MyPhone() # 这里不说new一个对象，说点啥子咧？？
phone.call_5g() # 直接调用了复写后的方法和属性
print(phone.producer)

"""
一旦复写，默认调用新的成员变量和成员方法
如果这时候需要使用父类的成员，采用一下方法：
方式1：
父类名.成员变量
父类名.成员方法(self)

方式2：
super().成员变量
super().成员方法()
"""