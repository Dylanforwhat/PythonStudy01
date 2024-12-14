"""
类和对象
"""
# 设计一个闹钟类
class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)

# 构建两个闹钟对象
clock1 = Clock()
clock1.id = "003032"
clock1.price= 19.99
print(f"id:{clock1.id},price:{clock1.price}")
clock1.ring()

clock2 = Clock()
clock2.id = "003033"
clock2.price= 23.99
print(f"id:{clock2.id},price:{clock2.price}")
clock2.ring()