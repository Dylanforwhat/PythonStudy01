money = 5000000
name = input("please input your name :")


def main_menu():
    print(f"""hi!{name}
    welcome to Heima Bank,menu:
    balance inquiry\t\t>>>1
    save money\t\t\t>>>2
    withdraw money\t\t>>>3
    exit\t\t\t\t>>>4
    """)
    return input("please input your choose:")


def balance_inquiry():
    print(f"balance money is {money}")


def save_money():
    x = input("please put in the money :")
    s = int(x)

    global money
    money += s
    print(f"Mr/Mrs{name},save {s} success!")
    balance_inquiry()

def withdraw_money():
    x = input("please take out the money :")
    s = int(x)

    global money
    money -= s
    print(f"Mr/Mrs{name},withdraw {s} success!")
    balance_inquiry()


while True: #  无限循环，这个要注意

    key_input = main_menu()
    if key_input == "1":
        balance_inquiry()
        continue #  通过continue进入下一次循环
    elif key_input == "2":
        save_money()
        continue
    elif key_input =="3":
        withdraw_money()
        continue
    else:
        print("exit!")
        break # 退出while True的无限循环





