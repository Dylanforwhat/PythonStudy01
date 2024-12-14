import random

j= 10000

for i in range(1,21):
    num = random.randint(1, 10)
    if num < 5:
        print(f"员工{i},绩效为{num},不发工资")
        continue
    else:
        j -= 1000
        print(f"员工{i},绩效为{num},发工资1000，账户余额{j}")
        if j == 0:
            break
