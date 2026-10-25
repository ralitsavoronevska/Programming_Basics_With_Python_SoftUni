number_of_loads = int(input())
MICROBUS_TON_PRICE = 200
TRUCK_TON_PRICE = 175
TRAIN_TON_PRICE = 120

train_cargo = 0
train_tonnage = 0
truck_cargo = 0
truck_tonnage = 0
total_tonnage = 0
microbus_cargo = 0
microbus_tonnage = 0
average_tonnage = 0

for cargo in range(1, number_of_loads + 1):
    cargo_tonnage = int(input())

    if 12 <= cargo_tonnage:
        train_tonnage += cargo_tonnage
    if 11 >= cargo_tonnage >= 4:
        truck_tonnage += cargo_tonnage
    if cargo_tonnage <= 3:
        microbus_tonnage += cargo_tonnage

total_tonnage += train_tonnage + truck_tonnage + microbus_tonnage
average_tonnage = ((train_tonnage * TRAIN_TON_PRICE) + (truck_tonnage * TRUCK_TON_PRICE) + (microbus_tonnage * MICROBUS_TON_PRICE)) / total_tonnage
train_cargo = train_tonnage / total_tonnage * 100
truck_cargo = truck_tonnage / total_tonnage * 100
microbus_cargo = microbus_tonnage / total_tonnage * 100

print(f"{average_tonnage:.2f}")
print(f"{microbus_cargo:.2f}%")
print(f"{truck_cargo:.2f}%")
print(f"{train_cargo:.2f}%")