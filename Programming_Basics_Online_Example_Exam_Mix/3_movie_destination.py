# https://alpha.judge.softuni.org/contests/03-movie-destination/1699/practice#5

budget = float(input())
destination = str(input())
season = str(input())
days = int(input())

film_options = {
    "Dubai": {
        "Summer": 40_000,
        "Winter": 45_000,
    },
    "Sofia": {
        "Summer": 12_500,
        "Winter": 17_000,
    },
    "London": {
        "Summer": 20_250,
        "Winter": 24_000,
    }
}

total_cost = 0

if destination in film_options and season in film_options[destination]:
    price_per_day = film_options[destination][season]
    total_cost += price_per_day * days

    if destination == "Dubai":
        total_cost -= total_cost * 0.3
    elif destination == "Sofia":
        total_cost += total_cost * 0.25

diff = abs(budget - total_cost)

if budget >= total_cost:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")