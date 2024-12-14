"""
if elif else 判断语句的使用
"""
height = int(input("input your height: "))
vip_level = int(input("input your level(1-5): "))

# if height < 120:
#     print("free for ticket")
if int(input("input your height: ")) < 120:
    print("free for ticket")
    

elif vip_level > 3:
    print("free for ticket")
else:
    print("please buy ticket")
