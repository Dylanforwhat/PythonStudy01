class AC:
    def cool(self):
        pass # 空实现
    def hot(self):
        pass
    def swing(self):
        pass

class MideaAC(AC):
    def cool(self):
        print("Midea cool")
    def hot(self):
        print("Midea hot")
    def swing(self):
        print("Midea swing")

class GREEAC(AC):
    def cool(self):
        print("GREE cool")
    def hot(self):
        print("GREE hot")
    def swing(self):
        print("GREE swing")

def make_cool(ac : AC):
    ac.cool()

Midea001 = MideaAC()
GREE001 = GREEAC()

make_cool(Midea001)
make_cool(GREE001)
