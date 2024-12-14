def f(n):
    for i in range(1,n+1):
        yield i
for i in f(2):
    print(i,end=' ')
