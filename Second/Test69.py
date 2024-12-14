class E(Exception):
    def __init__(self,message):
        self.message = message
    def __str__(self):
        return "its nice to see you"
try:
    print("I feel fine")
    raise E("what a pity")
except E as e:
    print(e)
else:
    print("the show must go on")