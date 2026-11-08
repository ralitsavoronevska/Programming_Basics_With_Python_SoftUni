from math import ceil

football_fan_name = str(input())
budget = float(input())
beer_bottles_count = int(input())
chips_packets_count = int(input())

BEER_PRICE = 1.20
beer_cost = BEER_PRICE * beer_bottles_count
CHIPS_PACKET_PRICE = beer_cost * 0.45
chips_cost = ceil(CHIPS_PACKET_PRICE * chips_packets_count)

total_cost = beer_cost + chips_cost

if total_cost <= budget:
    print(f"{football_fan_name} bought a snack and has {budget - total_cost:.2f} leva left.")
else:
    print(f"{football_fan_name} needs {total_cost - budget:.2f} more leva!")