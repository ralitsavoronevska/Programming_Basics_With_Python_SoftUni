# https://alpha.judge.softuni.org/contests/01-fruit-market/1654/practice#1

strawberries_price = float(input()) # leva
bananas_quantity = float(input()) # kg
oranges_quantity = float(input()) #kg
raspberries_quantity = float(input()) #kg
strawberries_quantity = float(input()) #kg

raspberries_price = strawberries_price / 2
oranges_price = raspberries_price - (raspberries_price * 0.4)
bananas_price = raspberries_price - (raspberries_price * 0.8)

total_price = (strawberries_quantity * strawberries_price) + (bananas_quantity * bananas_price) + (oranges_quantity * oranges_price) + (raspberries_quantity * raspberries_price)

print(f"{total_price:.2f}")