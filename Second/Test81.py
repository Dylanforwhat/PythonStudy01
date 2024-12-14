m = 0


def foo(n):
    global m
    assert m != 0
    try:
        return 1 / n
    except ArithmeticError:
        raise ValueError


try:
    foo(0)
except ArithmeticError:
    m += 2
except:
    m += 1

print(m)
