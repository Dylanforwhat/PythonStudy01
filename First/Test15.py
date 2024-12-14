"""
判断语句实战案例
终极猜数字
"""
import random
num = random.randint(1,10)

guess_num = int(input("input your number: "))

if guess_num == num:
    print("congratulations,1bingo")
else:
    if guess_num > num:
        print("big")
    else:
        print("small")
    guess_num = int(input("input again: "))
    if guess_num == num:
        print("congratulations,2bingo")
    else:
        if guess_num > num:
            print("big")
        else:
            print("small")

        guess_num = int(input("input again too: "))
        if guess_num == num:
            print("congratulations,bingo")
        else:
            print("finished")


