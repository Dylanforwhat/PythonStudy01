"""
异常的传递性
"""


def function1():
    print("function1 starts")
    num = 1 / 0
    print("function1 ends")


def function2():
    print("function2 starts")
    function1()
    print("function2 ends")


def main():
    try:
        function2()
    except Exception as e:
        print("exception capture!")

main()
