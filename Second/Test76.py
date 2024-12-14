def f(x):
    def g(x):
        return x*x
    return g

a = f(2)
b = f(3)
print(a(2))