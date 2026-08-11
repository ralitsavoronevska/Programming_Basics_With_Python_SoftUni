town = str(input())
sales_volume = float(input())
trade_commission = 0

cities = {
    "Sofia": [5, 7, 8, 12],
    "Varna": [4.5, 7.5, 10, 13],
    "Plovdiv": [5.5, 8, 12, 14.5]
}

if town not in cities:
    print("error")
elif sales_volume < 0:
    print("error")
else:
    if sales_volume <= 500:
        trade_commission = (sales_volume * cities[town][0]) / 100
    elif sales_volume <= 1000:
        trade_commission = (sales_volume * cities[town][1]) / 100
    elif sales_volume <= 10000:
        trade_commission = (sales_volume * cities[town][2]) / 100
    else:  # sales_volume > 10000
        trade_commission = (sales_volume * cities[town][3]) / 100

    print(f"{trade_commission:.2f}")