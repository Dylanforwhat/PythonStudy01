# 获取1-100一个随机数字
import random
num = random.randint(1,100)

count = 0
flag = True
while flag:
    guess_num = int(input("please input your guess number："))
    count += 1
    if guess_num == num:
        print("bingo!")
        flag = False
    else:
        if guess_num > num:
            print("big")
        else:
            print("small")
print(f"total{count}times")