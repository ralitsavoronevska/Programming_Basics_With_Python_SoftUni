ONE_KILO_FOOD = 12.45

small_cats_count = 0
medium_cats_count = 0
big_cats_count = 0
total_food = 0

cat_count = int(input())

for cat in range(cat_count):
    food = float(input())

    if 300 <= food <= 400:
        big_cats_count += 1
    elif 200 <= food <= 300:
        medium_cats_count += 1
    elif 100 <= food <= 200:
        small_cats_count += 1
    total_food += food

food_cost = total_food / 1000 * ONE_KILO_FOOD

print(f"Group 1: {small_cats_count} cats.")
print(f"Group 2: {medium_cats_count} cats.")
print(f"Group 3: {big_cats_count} cats.")
print(f"Price for food per day: {food_cost:.2f} lv.")