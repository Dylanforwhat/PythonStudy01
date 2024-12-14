s = "2A"
try:
    n = int(s)
except ValueError:
    n = 2
except ArithmeticError:
    n = 1
except:
    n = 0
print(n)