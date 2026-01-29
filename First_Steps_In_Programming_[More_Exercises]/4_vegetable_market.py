vegetables_price = float(input())
fruits_price = float(input())
vegetables_kilos = int(input())
fruits_kilos = int(input())

vegetables_cost = vegetables_price * vegetables_kilos
fruits_cost = fruits_price * fruits_kilos
total_cost = vegetables_cost + fruits_cost
total_cost_in_euros = total_cost / 1.94
print(f"{total_cost_in_euros:.2f}")