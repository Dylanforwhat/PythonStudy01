def f(x,y):
    nom,denom = x,y
    def g():
        return nom/denom
    return g

a = f(1,2)
b = f(3,4)

print(a(),b())