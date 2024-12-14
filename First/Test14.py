if int(input("your height :"))>120:
    print("buy ticket")
    print("if level > 3 ,free")
    if int(input("vip level :"))>3:
        print("free for ticket")
    else:
        print("buy ticket")
else:
    print("free for ticket")