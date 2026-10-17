season = str(input())
km_per_month = float(input())

km_rates = {
    "Spring": {
        "small_distance": 0.75,
        "medium_distance": 0.95,
        "large_distance": 1.45
    },
    "Summer": {
        "small_distance": 0.90,
        "medium_distance": 1.10,
        "large_distance": 1.45
    },
    "Autumn": {
        "small_distance": 0.75,
        "medium_distance": 0.95,
        "large_distance": 1.45
    },
    "Winter": {
        "small_distance": 1.05,
        "medium_distance": 1.25,
        "large_distance": 1.45
    }
}

distance_type = ""
index = 0

if season in list(km_rates.keys()):
    if km_per_month <= 5000:
        index = 0
    if 5000 < km_per_month <= 10000:
        index = 1
    if 10000 < km_per_month <= 20000:
        index = 2
    distance_type = list(km_rates[season].keys())[index]
    km_rate = km_rates[season][distance_type]
    drivers_salary = km_per_month * km_rate * 4 * 0.9
    print(f"{drivers_salary:.2f}")
else:
    print("Invalid season!")