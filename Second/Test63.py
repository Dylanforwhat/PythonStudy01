"""
继承
"""


# 单继承

class Phone:
    IMEI = None
    producer = "HM"

    def call_4g(self):
        print("4g is calling!")


class Phone2024(Phone):
    face_id = "10001"

    def call_5g(self):
        print("5g is calling!")


phone01 = Phone2024()
print(phone01.producer)
phone01.call_4g()
phone01.call_5g()


# 多继承

class NFCReader:
    nfc_type = "type5"
    producer = "HM"

    def read(self):
        print("NFC is reading!")

    def write(self):
        print("NFC is writing!")


class RemoteControl:
    rc_type = "typeN"

    def control(self):
        print("RC is running!")


class MyPhone(Phone, NFCReader, RemoteControl):  # 如果多个父类中有同名属性，调用的时候按左到右的顺序优先
    pass  # 补全语法(占位语句)，目的是不产生语法错误


phone = MyPhone()
phone.call_4g()
phone.read()
phone.write()
phone.control()
