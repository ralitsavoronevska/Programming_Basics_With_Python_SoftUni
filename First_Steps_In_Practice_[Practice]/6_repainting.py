amount_of_nylon = int(input())
amount_of_paint = int(input())
amount_of_thinner = int(input())
working_hours = int(input())

nylon_price_for_square_meter = 1.50
paint_price_per_liter = 14.50
thinner_price_per_liter = 5.00
price_of_bags = 0.40

total_nylon_price = (amount_of_nylon + 2) * nylon_price_for_square_meter
total_paint_price = (amount_of_paint + (amount_of_paint * (10/100))) * paint_price_per_liter
total_thinner_price = amount_of_thinner * thinner_price_per_liter
total_amount_for_materials = total_nylon_price + total_paint_price + total_thinner_price + price_of_bags
total_amount_for_craftsmen_work = (total_amount_for_materials * (30/100)) * working_hours
total_amount = total_amount_for_materials + total_amount_for_craftsmen_work

print(total_amount)
