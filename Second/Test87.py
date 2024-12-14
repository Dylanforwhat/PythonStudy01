def f(n):
    if n == 1:
        return '1'
    return  str(n)+f(n-1)

print(f(2))