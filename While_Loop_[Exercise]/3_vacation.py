needed_money = float(input())
balance = float(input())

days = 0
spending_days = 0

while spending_days < 5:
    act = input()
    amount = float(input())

    days += 1

    if act == "spend":
        spending_days += 1
        balance = max(0, balance - amount)
    elif act == "save":
        spending_days = 0
        balance += amount

        if balance >= needed_money:
            print(f"You saved the money for {days} days.")
            break
else:
    print(f"You can't save the money.")
    print(days)