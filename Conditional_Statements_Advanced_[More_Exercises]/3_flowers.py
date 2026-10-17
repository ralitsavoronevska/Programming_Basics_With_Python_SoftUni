chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = str(input())
holiday = str(input())

flowers_price_list = {
    "Spring": [2.00, 4.10, 2.50],
    "Summer": [2.00, 4.10, 2.50],
    "Autumn": [3.75, 4.50, 4.15],
    "Winter": [3.75, 4.50, 4.15]
}

arranging_a_bouquet = 2
chrysanthemums_price = 0
roses_price = 0
tulips_price = 0
bouquet_price = 0
all_flowers_count = chrysanthemums_count + roses_count + tulips_count

# Discounts and holiday prices list
spring_tulips = 0.95
winter_roses = 0.90
all_seasons_discount = 0.80
holiday_increase = 0.15

if season in flowers_price_list:
    chrysanthemums_price = chrysanthemums_count * flowers_price_list[season][0]
    roses_price = roses_count * flowers_price_list[season][1]
    tulips_price = tulips_count * flowers_price_list[season][2]
    bouquet_price = chrysanthemums_price + roses_price + tulips_price
    # holiday Increase
    if holiday == "Y":
        bouquet_price += bouquet_price * holiday_increase
    else:
        pass
    # Discounts
    if tulips_count > 7 and season == "Spring":
        bouquet_price *= spring_tulips
    if roses_count >= 10 and season == "Winter":
        bouquet_price *= winter_roses
    if all_flowers_count > 20:
        bouquet_price *= all_seasons_discount
    bouquet_price += arranging_a_bouquet
    print(f"{bouquet_price:.2f}")
else:
    print("Invalid season!")