budget = int(input())
season = str(input())
number_of_fishermen = int(input())

SPRING_SHIP_RENT = 3000
SUMMER_AND_AUTUMN_SHIP_RENT = 4200
WINTER_SHIP_RENT = 2600

price_for_rent = 0

if season == "Spring":
    price_for_rent = SPRING_SHIP_RENT
    if number_of_fishermen <= 6:
        price_for_rent -= price_for_rent * 0.1
    elif 7 <= number_of_fishermen <= 11:
        price_for_rent -= price_for_rent * 0.15
    elif number_of_fishermen >= 12:
        price_for_rent -= price_for_rent * 0.25
elif season == "Summer" or season == "Autumn":
    price_for_rent = SUMMER_AND_AUTUMN_SHIP_RENT
    if number_of_fishermen <= 6:
        price_for_rent -= price_for_rent * 0.1
    elif 7 <= number_of_fishermen <= 11:
        price_for_rent -= price_for_rent * 0.15
    elif number_of_fishermen >= 12:
        price_for_rent -= price_for_rent * 0.25
elif season == "Winter":
    price_for_rent = WINTER_SHIP_RENT
    if number_of_fishermen <= 6:
        price_for_rent -= price_for_rent * 0.1
    elif 7 <= number_of_fishermen <= 11:
        price_for_rent -= price_for_rent * 0.15
    elif number_of_fishermen >= 12:
        price_for_rent -= price_for_rent * 0.25

if season != "Autumn" and number_of_fishermen % 2 == 0:
    price_for_rent -= price_for_rent * 0.05

money_left = abs(budget - price_for_rent)

if budget >= price_for_rent:
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_left:.2f} leva.")