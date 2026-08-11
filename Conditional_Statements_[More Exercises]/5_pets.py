# Input:
# брой дни – цяло число в интервал [1…5000]
# оставена храна в килограми – цяло число в интервал [0…100000]
# храна на ден за кучето в килограми – реално число в интервал [0.00…100.00]
# храна на ден за котката в килограми– реално число в интервал [0.00…100.00]
# храна на ден за костенурката в грамове – реално число в интервал [0.00…10000.00]

from math import floor
from math import ceil

number_of_days = int(input())
total_food_in_kg = int(input())
dog_food_per_day_in_kg = float(input())
cat_food_per_day_in_kg = float(input())
turtle_food_per_day_in_grams = float(input())

dog_food_needed_for_day = dog_food_per_day_in_kg * number_of_days
cat_food_needed_for_day = cat_food_per_day_in_kg * number_of_days
turtle_food_needed_for_day = (turtle_food_per_day_in_grams * number_of_days) / 1000

total_food_needed_for_day = dog_food_needed_for_day + cat_food_needed_for_day + turtle_food_needed_for_day

diff = abs(total_food_needed_for_day - total_food_in_kg)

if total_food_needed_for_day <= total_food_in_kg:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed.")