"""
变量的类型注解

变量：类型
*基础数据类型;  例：var_1:int = 10
*类对象类型;   例：stu:Student = Student()
*基础容器类型; 例：my_list:list = [1,2,3,4]  / my_dict:dict[str,int] = {"itheima":666}

*在注释中进行类型注解
class Student：
    pass
 var_1 = random.randint(1,10)  # type:int


 类型注解是一种备注，写错了也不会影响程序运行！
"""
import random

var_1 = random.randint(1, 10)  # type: int

#  Union联合类型注解
from typing import Union

my_list: list[Union[int, str]] = [1, 2, "itheima", "itcast"]
