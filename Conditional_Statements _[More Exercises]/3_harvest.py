# Input:
# X кв.м е лозето – цяло число в интервала [10 … 5000]
# Y грозде за един кв.м – реално число в интервала [0.00 … 10.00]
# Z нужни литри вино – цяло число в интервала [10 … 600]
# брой работници – цяло число в интервала [1 … 20]

from math import ceil
from math import floor

x = int(input())
y = float(input())
wine_needed = int(input())
workers = int(input())

total_greap_area = x * y
wine_produced = (total_greap_area * 0.40) / 2.5
diff = abs(wine_produced - wine_needed)

if wine_produced < wine_needed:
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {ceil(wine_produced)} liters.")
    print(f"{ceil(diff)} liters left -> {ceil(diff / workers)} liters per person.")