"""
多种传参形式
位置参数
关键字参数
缺省参数
不定长参数
"""


def user_info(name, age, gender):
    print(name, age, gender)


user_info('xiaoming', 20, 'man')

user_info(age=40, gender='woman', name='xiaohong')


def user_info1(name, age, gender='man'):  # 设置默认函数或缺省函数的时候，要放在最后，不然报错
    print(name, age, gender)


user_info1('xiaotian', 13)


def user_info2(*args):
    print(type(args), args)


user_info2(1, 23, 4, "xiaoming")


def user_info3(**kwargs):
    print(type(kwargs), kwargs)


user_info3(a=1, b=3, c=123124, d="python")
