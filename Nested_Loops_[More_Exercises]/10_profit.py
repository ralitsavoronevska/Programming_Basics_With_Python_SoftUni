coins_1 = int(input())
coins_2 = int(input())
banknotes_5 = int(input())
total = int(input())

for one in range(coins_1 + 1):
    for two in range(coins_2 + 1):
        for five in range(banknotes_5 + 1):

            current_sum = one * 1 + two * 2 + five * 5

            if current_sum == total:
                print(f"{one} * 1 lv. + {two} * 2 lv. + {five} * 5 lv. = {total} lv.")