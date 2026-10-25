total_game_moves = int(input())

from_0_to_9_numbers = 0
from_10_to_19_numbers = 0
from_20_to_29_numbers = 0
from_30_to_39_numbers = 0
from_40_to_50_numbers = 0
invalid_numbers = 0
result = 0

for move in range(1, total_game_moves + 1):
    new_number = int(input())

    if 40 <= new_number <= 50:
        from_40_to_50_numbers += 1
        result += 100
    if 30 <= new_number <= 39:
        from_30_to_39_numbers += 1
        result += 50
    if 20 <= new_number <= 29:
        from_20_to_29_numbers += 1
        result += new_number * 40 / 100
    if 10 <= new_number <= 19:
        from_10_to_19_numbers += 1
        result += new_number * 30 / 100
    if 0 <= new_number <= 9:
        from_0_to_9_numbers += 1
        result += new_number * 20 / 100
    if new_number < 0 or new_number > 50:
        invalid_numbers += 1
        result /= 2

from_0_to_9_numbers_percentage = from_0_to_9_numbers / total_game_moves * 100
from_10_to_19_numbers_percentage = from_10_to_19_numbers / total_game_moves * 100
from_20_to_29_numbers_percentage = from_20_to_29_numbers / total_game_moves * 100
from_30_to_39_numbers_percentage = from_30_to_39_numbers / total_game_moves * 100
from_40_to_50_numbers_percentage = from_40_to_50_numbers / total_game_moves * 100
invalid_numbers_percentage = invalid_numbers / total_game_moves * 100

print(f"{result:.2f}")
print(f"From 0 to 9: {from_0_to_9_numbers_percentage:.2f}%")
print(f"From 10 to 19: {from_10_to_19_numbers_percentage:.2f}%")
print(f"From 20 to 29: {from_20_to_29_numbers_percentage:.2f}%")
print(f"From 30 to 39: {from_30_to_39_numbers_percentage:.2f}%")
print(f"From 40 to 50: {from_40_to_50_numbers_percentage:.2f}%")
print(f"Invalid numbers: {invalid_numbers_percentage:.2f}%")
