"""
包package
必须在'__init__.py'文件中添加'__all__ = []' 来控制允许允许导入的module列表（仅限于import*操作）
（类似java的权限修饰符public、protected、private）
"""
from others import *
# mymodule01() # 被权限控制，无法使用
mymodule02()