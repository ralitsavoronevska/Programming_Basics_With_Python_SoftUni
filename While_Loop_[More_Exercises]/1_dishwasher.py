BOTTLE_WASHING_LIQUID = 750
DISH_WASHING_LIQUID = 5
POT_WASHING_LIQUID = 15

number_of_bottles = int(input())
total_washing_liquid = number_of_bottles * BOTTLE_WASHING_LIQUID
index = 1
dishes = 0
pots = 0

while True:
    number_kitchenware_to_wash = input()

    if number_kitchenware_to_wash == "End":
        break

    kitchenware = int(number_kitchenware_to_wash)

    if index % 3 == 0:
        pots += kitchenware
        total_washing_liquid -= kitchenware * POT_WASHING_LIQUID
    else:
        dishes += kitchenware
        total_washing_liquid -= kitchenware * DISH_WASHING_LIQUID

    index += 1

    if total_washing_liquid < 0:
        break

if total_washing_liquid >= 0:
    print("Detergent was enough!")
    print(f"{dishes} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {total_washing_liquid} ml.")
else:
    print(f"Not enough detergent, {abs(total_washing_liquid)} ml. more necessary!")