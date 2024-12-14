import random
inputstr = input().split()
N = int(inputstr[0])
K = int(inputstr[1])
list1 = [random.randint(0,9999) for _ in range(N)]
list2 = [random.randint(0,9999) for _ in range(K)]
print(list1)
print(list2)

for index,item in enumerate(list2):
    if item in list2:
        print(index)
else:
    print("-1")