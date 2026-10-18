budget_bulgaria_limit = 100
budget_balkans_limit = 1000

budget = float(input())
season = str(input())

destination = ""
type_of_vacation = ""
amount_spent = 0

if season == "summer":
    if budget <= budget_bulgaria_limit:
        destination = "Bulgaria"
        amount_spent = budget * 0.3
        type_of_vacation = "Camp"
    if 100 < budget <= budget_balkans_limit:
        destination = "Balkans"
        amount_spent = budget * 0.4
        type_of_vacation = "Camp"
    if budget > budget_balkans_limit:
        destination = "Europe"
        amount_spent = budget * 0.9
        type_of_vacation = "Hotel"
elif season == "winter":
    if budget <= budget_bulgaria_limit:
        destination = "Bulgaria"
        amount_spent = budget * 0.7
        type_of_vacation = "Hotel"
    if 100 < budget <= budget_balkans_limit:
        destination = "Balkans"
        amount_spent = budget * 0.8
        type_of_vacation = "Hotel"
    if budget > budget_balkans_limit:
        destination = "Europe"
        amount_spent = budget * 0.9
        type_of_vacation = "Hotel"

print(f"Somewhere in {destination}")
print(f"{type_of_vacation} - {amount_spent:.2f}")