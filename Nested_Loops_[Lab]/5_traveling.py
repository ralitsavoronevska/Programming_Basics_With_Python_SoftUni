while True:
    destination = str(input())

    if destination == "End":
        break

    budget = float(input())
    saved_money = 0.0

    while saved_money < budget:
        new_amount = float(input())
        saved_money += new_amount

    print(f"Going to {destination}!")