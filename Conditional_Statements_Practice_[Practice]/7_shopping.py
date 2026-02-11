# Input
# 1. Бюджетът на Петър - реално число в интервала [1.0…100000.0]
# 2. Броят видеокарти - цяло число в интервала [1…100]
# 3. Броят процесори - цяло число в интервала [1…100]
# 4. Броят рам памет - цяло число в интервала [1…100]
from platform import processor

budget = float(input())
video_cards_amount = int(input())
processors_amount = int(input())
ram_memory_amount = int(input())

video_cards_price = 250
video_cards_cost = video_cards_amount * video_cards_price
processors_price = video_cards_cost * 0.35
ram_memory_price = video_cards_cost * 0.10

processors_cost = processors_amount * processors_price
ram_memory_cost = ram_memory_amount * ram_memory_price

total_cost = video_cards_cost + processors_cost + ram_memory_cost

if video_cards_amount > processors_amount:
    total_cost -= total_cost * 0.15

diff = abs(budget - total_cost)

if budget >= total_cost:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")