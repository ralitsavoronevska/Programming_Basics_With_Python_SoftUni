chicken_menu_amount = int(input())
fish_menu_amount = int(input())
vegetarian_menu_amount = int(input())

chicken_menu_price = 10.35
fish_menu_price = 12.40
vegetarian_menu_price = 8.15
delivery_price = 2.50

total_chicken_menus_price = chicken_menu_amount * chicken_menu_price
total_fish_menus_price = fish_menu_amount * fish_menu_price
total_vegetarian_menus_price = vegetarian_menu_amount * vegetarian_menu_price
total_menus_price = total_chicken_menus_price + total_fish_menus_price + total_vegetarian_menus_price
dessert_price = total_menus_price * (20/100)
total_price = (total_menus_price + dessert_price + delivery_price)

print(f"{total_price:.2f}")
