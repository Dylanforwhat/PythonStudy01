"""
外层：表白100天的控制
内层：每天都送10朵玫瑰花的控制

"""
i = 1
while i <= 100:
     print(f"today is {i}days,ready to do it!")

     j = 1
     while j <= 10:
         print(f"scend meimei {j} rose")
         j += 1
     print("meimei, I love you!")
     i += 1

print(f"until {i - 1}day success")