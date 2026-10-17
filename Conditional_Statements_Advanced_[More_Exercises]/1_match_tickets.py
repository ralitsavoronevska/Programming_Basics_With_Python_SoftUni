budget = float(input())
ticket_category = str(input())
number_of_people_per_group = int(input())

vip_tickets_price = 499.99
normal_tickets_price = 249.99
transport_cost = 0

if 1 <= number_of_people_per_group <= 4:
    transport_cost = budget * 0.75
elif 5 <= number_of_people_per_group <= 9:
    transport_cost = budget * 0.60
elif 10 <= number_of_people_per_group <= 24:
    transport_cost = budget * 0.50
elif 25 <= number_of_people_per_group <= 49:
    transport_cost = budget * 0.40
elif 50 <= number_of_people_per_group:
    transport_cost = budget * 0.25

ticket_budget = budget - transport_cost

if ticket_category == "Normal":
    money_needed = number_of_people_per_group * normal_tickets_price
    money_left = ticket_budget - money_needed
    if money_needed <= ticket_budget:
        print(f"Yes! You have {money_left:.2f} leva left.")
    else:
        print(f"Not enough money! You need {abs(money_left):.2f} leva.")
elif ticket_category == "VIP":
    money_needed = number_of_people_per_group * vip_tickets_price
    money_left = ticket_budget - money_needed
    if money_needed <= ticket_budget:
        print(f"Yes! You have {money_left:.2f} leva left.")
    else:
        print(f"Not enough money! You need {abs(money_left):.2f} leva.")