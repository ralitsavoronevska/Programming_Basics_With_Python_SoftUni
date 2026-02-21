# Prices for fuel:
# Gasoline 2.22lv per liter
# Diesel 2.33lv per liter
# Gas 0.93lv per liter

# Discount for fuel if the driver has a discount card:
# Gasoline 0.18lv per liter
# Diesel 0.12lv per liter
# gas 0.08lv per liter

# Ако шофьора е заредил между 20 и 25 литра включително, той получава 8 процента отстъпка от крайната цена,
# при повече от 25 литра гориво, той получава 10 процента отстъпка от крайната цена.

# Input:
# Типа на горивото – текст с възможности: "Gas", "Gasoline" или "Diesel"
# Количество гориво – реално число в интервала [1.00 … 50.00]
# Притежание на клубна карта – текст с възможности: "Yes" или "No"

type_of_fuel = str(input())
liters_of_fuel = float(input())
has_club_card = str(input())

liter_of_gasoline = 2.22
liter_of_diesel = 2.33
liter_of_gas = 0.93

discount_for_gasoline = 0.18
discount_for_diesel = 0.12
discount_for_gas = 0.08

discount_for_20_to_25 = 0.08
discount_for_more_than_25 = 0.1

if type_of_fuel == "Gasoline":
    base_price = liter_of_gasoline
elif type_of_fuel == "Diesel":
    base_price = liter_of_diesel
else:  # Gas
    base_price = liter_of_gas

if has_club_card == "Yes":
    if type_of_fuel == "Gasoline":
        final_price_per_liter = base_price - discount_for_gasoline
    elif type_of_fuel == "Diesel":
        final_price_per_liter = base_price - discount_for_diesel
    else:  # Gas
        final_price_per_liter = base_price - discount_for_gas
else:
    final_price_per_liter = base_price

total_price = final_price_per_liter * liters_of_fuel

if 20 <= liters_of_fuel <= 25:
    total_price -= total_price * discount_for_20_to_25
elif liters_of_fuel > 25:
    total_price -= total_price * discount_for_more_than_25
print(f"{total_price:.2f} lv.")