screening_type = str(input())
rows = int(input())
columns = int(input())

income = 0
cinema_capacity = rows * columns
PREMIERE_PRICE = 12.00
NORMAL_PRICE = 7.50
DISCOUNT_PRICE = 5.00

if screening_type == 'Premiere':
    income = cinema_capacity * PREMIERE_PRICE
elif screening_type == 'Normal':
    income = cinema_capacity * NORMAL_PRICE
elif screening_type == 'Discount':
    income = cinema_capacity * DISCOUNT_PRICE

print(f"{income:.2f} leva")