dog_food = int(input()) * 1000
needed_food = 0

while True:
    command = input()

    if command == "Adopted":
        break

    food_per_day = int(command)

    needed_food += food_per_day

if dog_food >= needed_food:
    print(f"Food is enough! Leftovers: {dog_food - needed_food} grams.")
else:
    print(f"Food is not enough. You need {needed_food - dog_food} grams more.")