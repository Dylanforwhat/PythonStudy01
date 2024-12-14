def test_function(comp):
    result = comp(1, 2)
    print(result)


def comp(x, y):
    return x + y


test_function(comp)


# lambda 匿名函数演示
def test_function1(comp):
    result = comp(1, 2)
    print(result)
test_function1(lambda x, y: x + y)  # lambda 只能写一行
