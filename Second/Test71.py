class Class:
    Variable = 0
    def __init__(self):
        self.value = 0
object1 = Class()
Class.Variable += 1

object2 = Class()
object2.value += 1

print(object2.Variable)
print(object1.value)