movie_budget = float(input())
extras_amount = int(input())
price_for_clothing_per_extra = float(input())

decoration = movie_budget * 0.10

if extras_amount > 150:
    price_for_clothing_per_extra -= price_for_clothing_per_extra * 0.10

total_amount_needed = price_for_clothing_per_extra * extras_amount

if (decoration + total_amount_needed) > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {(decoration + total_amount_needed) - movie_budget:.2f} leva more.")
if (decoration + total_amount_needed) <= movie_budget:
    print("Action!")
    print(f"Wingard starts filming with {movie_budget - (decoration + total_amount_needed):.2f} leva left.")
