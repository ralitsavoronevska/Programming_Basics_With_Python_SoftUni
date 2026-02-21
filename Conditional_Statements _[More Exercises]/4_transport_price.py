# n kilometers

# 3 types of transport:

# taxi:
# initiation fee 0.70lv
# daily rate 0.79lv/km
# night rate 0.90lv/km

# bus:
# daily rate / night rate 0.09lv/km
# Can be used for distances of a minimum of 20km

# train:
# daily rate / night rate 0.06lv/km
# Can be used for distances of a minimum of 100km

# Input
n = int(input())
travel_period = str(input())

min_price = float('inf')

if n < 20:
    # taxi
    if travel_period == "day":
        price = ((n * 0.79) + 0.70)
    else:
        price = ((n * 0.90) + 0.70)
    min_price = price
elif 20 <= n < 100:
    # bus
    price = n * 0.09
    min_price = min(min_price, price)
else:
    # train
    price = n * 0.06
    min_price = min(min_price, price)

print(f"{min_price:.2f}")