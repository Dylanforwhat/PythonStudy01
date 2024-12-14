"""
异常的捕获（异常处理）


"""
try:
    f = open("d:/abc.txt","r",encoding = "UTF-8")
except:
    print("exception!")
    f = open("d:/abc.txt", "w", encoding="UTF-8")

"""
捕获指定异常
"""

try:
    print(name)
except NameError as e:  #e是这个异常的名字，可以打印异常类型
    print("出现了未定义的变量")
    print(e)

"""
捕获多个异常
"""

try:
    print(name)

except(NameError,ZeroDivisionError) as e:
    print("exception")

"""
捕获全部异常
"""
try:
    print(name)
except Exception as e:
    print("exception!")
else:
    print("no good")
finally:
    f.close()