budget = float(input())
season = str(input())

vacation_options = {
    "Summer": {
        "Camp": {
            "Alaska": 0.65
        },
        "Hut": {
            "Alaska": 0.80
        },
        "Hotel": {
            "Alaska": 0.90
        }
    },
    "Winter": {
        "Camp": {
            "Morocco": 0.45
        },
        "Hut": {
            "Morocco": 0.60
        },
        "Hotel": {
            "Morocco": 0.90
        }
    }
}

accommodation_type = ""
location = ""
percentage = 0
location_price = 0
index = 0

if season in list(vacation_options.keys()):
    if budget <= 1000:
        index = 0
    if 1000 < budget <= 3000:
        index = 1
    if 3000 < budget:
        index = 2
    accommodation_type = list(vacation_options[season].keys())[index]
    location = list(vacation_options[season][accommodation_type])[0]
    percentage = vacation_options[season][accommodation_type][location]
    location_price = budget * percentage
    print(f"{location} - {accommodation_type} - {location_price:.2f}")
else:
    print("Invalid season!")