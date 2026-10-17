season = str(input())
type_of_group = str(input())
number_of_students = int(input())
number_of_nights = int(input())

school_camp_info = {
    "Spring": {
        "boys": {
            "price per night": 7.20,
            "sport": "Tennis"
        },
        "girls": {
            "price per night": 7.20,
            "sport": "Athletics"
        },
        "mixed": {
            "price per night": 9.50,
            "sport": "Cycling"
        }
    },
    "Summer": {
        "boys": {
            "price per night": 15,
            "sport": "Football"
        },
        "girls": {
            "price per night": 15,
            "sport": "Volleyball"
        },
        "mixed": {
            "price per night": 20,
            "sport": "Swimming"
        }
    },
    "Winter": {
        "boys": {
            "price per night": 9.60,
            "sport": "Judo"
        },
        "girls": {
            "price per night": 9.60,
            "sport": "Gymnastics"
        },
        "mixed": {
            "price per night": 10,
            "sport": "Ski"
        }
    }
}

discount = 0
price_per_night = 0
sport = ""
total_cost = 0

if season in list(school_camp_info.keys()):
    if number_of_students >= 50:
        discount = .5
    elif 50 > number_of_students >= 20:
        discount = .15
    elif 20 > number_of_students >= 10:
        discount = .05

    price_per_night = school_camp_info[season][type_of_group]["price per night"]
    sport = school_camp_info[season][type_of_group]["sport"]
    cost = (price_per_night * number_of_nights * number_of_students)
    total_cost = cost - (cost * discount)
    print(f"{sport} {total_cost:.2f} lv.")
else:
    print("Invalid season!")
