# https://alpha.judge.softuni.org/contests/02-family-trip/1745/practice#2

budget = float(input())
nights = int(input())
price_per_night = float(input())
extra_percent = int(input()) / 100

if nights > 7:
    price_per_night -= price_per_night * 0.05

extra_cost = budget * extra_percent
total_cost = (nights * price_per_night) + extra_cost

diff = abs(budget - total_cost)

if total_cost <= budget:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")