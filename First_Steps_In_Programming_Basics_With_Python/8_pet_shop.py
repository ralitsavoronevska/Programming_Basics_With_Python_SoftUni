# Input
# 1. Броят на опаковките храна за кучета – цяло число в интервала [0… 100]
# 2. Броят на опаковките храна за котки –  цяло число в интервала [0… 100]
# Output
# "{total_sum} lv."

dog_food = int(input())
cat_food = int(input())
total_amount_dog_food = dog_food * 2.50
total_amount_cat_food = cat_food * 4
total_sum = total_amount_dog_food + total_amount_cat_food
print(f"{total_sum} lv.")

