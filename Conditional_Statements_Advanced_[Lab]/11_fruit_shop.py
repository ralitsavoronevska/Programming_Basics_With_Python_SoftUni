fruit = str(input())
day_of_the_week = str(input())
quantity = float(input())

working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]

prices = {
    "banana": [2.50, 2.70],
    "apple": [1.20, 1.25],
    "orange": [0.85, 0.90],
    "grapefruit": [1.45, 1.60],
    "kiwi": [2.70, 3.00],
    "pineapple": [5.50, 5.60],
    "grapes": [3.85, 4.20],
}

if fruit not in prices or day_of_the_week not in working_days + weekend:
    print("error")
else:
    price = prices[fruit][0] if day_of_the_week in working_days else prices[fruit][1]
    total_price = quantity * price
    print(f"{total_price:.2f}")