BROTHER_MONEY = 1

ages = int(input())
washing_machine_price = float(input())
unit_price_per_toy = int(input())

total_money = 0
count_toys = 0
increase_money_for_birth = 10

for age in range(1, ages + 1):
    if age % 2 == 0:
        total_money += (increase_money_for_birth - BROTHER_MONEY)
        increase_money_for_birth += 10
    else:
        count_toys += 1

total_money += (count_toys * unit_price_per_toy)

if total_money >= washing_machine_price:
    print(f"Yes! {total_money - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - total_money:.2f}")