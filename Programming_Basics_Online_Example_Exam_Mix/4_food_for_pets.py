# https://alpha.judge.softuni.org/contests/04-food-for-pets/2275/practice#8

days = int(input())
quantity_food = float(input())

total_food = 0
total_dog_food = 0
total_cat_food = 0
total_biscuits = 0

for day in range(1, days + 1):
    current_dog_food = int(input())
    current_cat_food = int(input())

    total_dog_food += current_dog_food
    total_cat_food += current_cat_food

    if day % 3 == 0:
        total_biscuits += (current_dog_food + current_cat_food) * 0.1

total_food = total_dog_food + total_cat_food
percent_eaten_food = (total_food / quantity_food) * 100
percent_eaten_cat_food = (total_cat_food / total_food) * 100
percent_eaten_dog_food = (total_dog_food / total_food) * 100

print(f"Total eaten biscuits: {round(total_biscuits)}gr.")
print(f"{percent_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_eaten_dog_food:.2f}% eaten from the dog.")
print(f"{percent_eaten_cat_food:.2f}% eaten from the cat.")