# magnolias: 3.25lv
# hyacinths: 4lv
# roses: 3.50lv
# cacti: 8lv

# Input:
# Брой магнолии – цяло число в интервала [0 … 50]
# Брой зюмбюли – цяло число в интервала [0 … 50]
# Брой рози – цяло число в интервала [0 … 50]
# Брой кактуси – цяло число в интервала [0 … 50]
# Цена на подаръка – реално число в интервала [0.00 … 500.00]

# * От общата сума, Мария трябва да плати 5% данъци.

from math import floor
from math import ceil

amount_of_magnolias = int(input())
amount_of_ziumbuli = int(input())
amount_of_roses = int(input())
amount_of_cacti = int(input())
price_of_gift = float(input())

cost_of_flowers = (amount_of_magnolias * 3.25) + (amount_of_ziumbuli * 4) + (amount_of_roses * 3.50) + (amount_of_cacti * 8)
sum_of_taxes = cost_of_flowers * 0.05
profit = cost_of_flowers - sum_of_taxes

if profit >= price_of_gift:
    print(f"She is left with {floor(profit - price_of_gift)} leva.")
else:
    print(f"She will have to borrow {ceil(price_of_gift - profit)} leva.")