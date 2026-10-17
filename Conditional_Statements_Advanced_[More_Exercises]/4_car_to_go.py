budget = float(input())
season = str(input())

car_lists = {
    "Summer": {
        "Economy class": {
            "Cabrio": 0.35,
        },
        "Compact class": {
            "Cabrio": 0.45
        },
        "Luxury class": {
            "Jeep": 0.90
        },
    },
    "Winter": {
        "Economy class": {
            "Jeep": 0.65
        },
        "Compact class": {
            "Jeep": 0.80
        },
        "Luxury class": {
            "Jeep": 0.90
        },
    }
}

car_class = ""
car_make = ""
percentage = 0
car_price = 0
index = 0

if season in list(car_lists.keys()):
    if budget <= 100:
        index = 0
    if 100 < budget <= 500:
        index = 1
    if 500 < budget:
        index = 2
    car_class = list(car_lists[season].keys())[index]
    car_make = list(car_lists[season][car_class])[0]
    percentage = car_lists[season][car_class][car_make]
    car_price = budget * percentage
    print(car_class)
    print(f"{car_make} - {car_price:.2f}")
else:
    print("Invalid season!")