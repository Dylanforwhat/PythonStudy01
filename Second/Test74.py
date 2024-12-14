class Class:
    data = 1
    def __init__(self,value):
        self.prop = self.var = value
Object = Class(2)

print(Object.__dict__)
print(Class.__dict__)