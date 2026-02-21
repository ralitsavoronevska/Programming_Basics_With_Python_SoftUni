type_of_fuel = str(input())
liters_of_fuel = float(input())

if type_of_fuel != "Diesel" and type_of_fuel != "Gasoline" and type_of_fuel != "Gas":
    print("Invalid fuel!")
elif liters_of_fuel >= 25:
    print(f"You have enough {type_of_fuel.lower()}.")
else:
    print(f"Fill your tank with {type_of_fuel.lower()}!")