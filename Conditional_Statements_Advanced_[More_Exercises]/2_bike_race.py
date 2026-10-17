junior_bikers = int(input())
senior_bikers = int(input())
route = str(input())

bikers = {
    "juniors": {
        "trail": 5.50,
        "cross-country": 8,
        "downhill": 12.25,
        "road": 20
    },
    "seniors": {
        "trail": 7,
        "cross-country": 9.50,
        "downhill": 13.75,
        "road": 21.50
    }
}

total_bikers = junior_bikers + senior_bikers

if route in bikers["juniors"]:
    total_junior_fees = bikers["juniors"][route] * junior_bikers
    total_senior_fees = bikers["seniors"][route] * senior_bikers
    total_fees = total_junior_fees + total_senior_fees

    if route == "cross-country" and total_bikers >= 50:
        total_fees *= 0.75  # 25% отстъпка

    total_fees *= 0.95

    print(f"{total_fees:.2f}")
else:
    print("Invalid route!")