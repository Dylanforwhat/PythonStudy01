class Test(object):
    def func(self):
        return '666'
print(Test().__module__)  # 输出当前类所在的模块
print(Test.__module__)    # 输出类本身所在的模块
print(Test.func.__module__)  # 输出方法所在的模块