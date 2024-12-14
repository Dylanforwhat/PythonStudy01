class ClassA:
    var = 1
    def __init__(self,prop):
        prop1 = prop2 = prop
    def __str__(self):
        return 'Object'

class ClassB(ClassA):
    def __init__(self,prop):
        prop3 = prop ** 2
        super().__init__(prop)

Object = ClassB(2)



print(len(ClassB.__bases__))
print(ClassA.__module__)
print(__name__)
print(str(Object))