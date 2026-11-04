puzzle_price = 2.60
talking_doll_price = 3
stuffed_teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2

excursion_price = float(input())
puzzle_amount = int(input())
talking_doll_amount = int(input())
stuffed_teddy_bear_amount = int(input())
minion_amount = int(input())
truck_amount = int(input())

puzzle_total = puzzle_amount * puzzle_price
talking_doll_total = talking_doll_amount * talking_doll_price
stuffed_teddy_bear_total = stuffed_teddy_bear_amount * stuffed_teddy_bear_price
minion_total = minion_amount * minion_price
truck_total = truck_amount * truck_price
amount_of_toys = puzzle_amount + talking_doll_amount + stuffed_teddy_bear_amount + minion_amount + truck_amount
total_toys_price = puzzle_total + talking_doll_total + stuffed_teddy_bear_total + minion_total + truck_total

if amount_of_toys >= 50:
    total_toys_price -= total_toys_price * 0.25

rent = total_toys_price * 0.10
total_toys_price -= rent

if total_toys_price >= excursion_price:
    print(f"Yes! {(total_toys_price - excursion_price):.2f} lv left.")
else:
    print(f"Not enough money! {(excursion_price - total_toys_price):.2f} lv needed.")