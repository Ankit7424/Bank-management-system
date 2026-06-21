balance = 100000

while True:
    print("1.deposit")
    print("2.withdrawal")
    print("3.check balance")
    print("4.exit")

    choice = int(input("enter your choice"))
    if choice == 1:
        amount = float(input("enter deposit amount"))
        balance += amount
        print("amount deposit successfully")

    elif choice ==2:
        amount = float(input("withdrwal amount"))
        if amount > balance:
            print("insufficient balance")
        else:
            balance -= amount
            print("withdrawal amount successfully")

    elif choice == 3:
        print("current balance =",balance)

    elif choice == 4:
        print("thankyou for banking service ")
        break


    else:
        print("invalid choice")


