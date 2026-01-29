h = float(input())
w = float(input())

final_w = ((w * 100) - 100) // 70
final_h = (h * 100) // 120
number_of_seats = (final_h * final_w) - 3

if 3 <= w <= h <= 100:
    print(int(number_of_seats))