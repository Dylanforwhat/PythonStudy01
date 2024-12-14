class A:
    __VarA = 1
    def get(self):
        return self.__VarA
class B(A):
    __VarA = 2
    def get(self):
        return self.__VarA
class C(A):
    __VarA = 3

obj_a = A()
obj_b = B()
obj_c = C()

