class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass

class Class2(A,B):
    pass
class Class3(A,C):
    pass
class Class1(D):
    pass
class Class4(C,B):
    pass
