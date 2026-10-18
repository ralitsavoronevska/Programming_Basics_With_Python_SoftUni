type_of_flowers = str(input())
quantity_of_flowers = int(input())
budget = int(input())

ROSES_PRICE = 5
DAHLIAS_PRICE = 3.80
TULIPS_PRICE = 2.80
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.50

total_price = 0

if type_of_flowers == "Roses":
    total_price = quantity_of_flowers * ROSES_PRICE
    if quantity_of_flowers > 80:
        total_price -= total_price * 0.10
elif type_of_flowers == "Dahlias":
    total_price = quantity_of_flowers * DAHLIAS_PRICE
    if quantity_of_flowers > 90:
        total_price -= total_price * 0.15
elif type_of_flowers == "Tulips":
    total_price = quantity_of_flowers * TULIPS_PRICE
    if quantity_of_flowers > 80:
        total_price -= total_price * 0.15
elif type_of_flowers == "Narcissus":
    total_price = quantity_of_flowers * NARCISSUS_PRICE
    if quantity_of_flowers < 120:
        total_price += total_price * 0.15
elif type_of_flowers == "Gladiolus":
    total_price = quantity_of_flowers * GLADIOLUS_PRICE
    if quantity_of_flowers < 80:
        total_price += total_price * 0.20

money_left = abs(budget - total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {quantity_of_flowers} {type_of_flowers} and {money_left:.2f} leva left.")
else:
    print(f"Not enough money, you need {money_left:.2f} leva more.")