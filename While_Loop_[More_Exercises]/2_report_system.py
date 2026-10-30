expected_amount = int(input())

index = 1
total_cash_amount = 0
total_card_amount = 0
cash = 0
card = 0

while True:
    amount = input()

    if amount == "End":
        print("Failed to collect required money for charity.")
        break

    price = int(amount)

    if index % 2 != 0:
        if price > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            cash += 1
            total_cash_amount += price
    else:
        if price < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            card += 1
            total_card_amount += price

    index += 1

    total_amount = total_cash_amount + total_card_amount

    if total_amount >= expected_amount:
        average_cash_amount = total_cash_amount / cash if cash > 0 else 0
        average_card_amount = total_card_amount / card if card > 0 else 0
        print(f"Average CS: {average_cash_amount:.2f}")
        print(f"Average CC: {average_card_amount:.2f}")
        break