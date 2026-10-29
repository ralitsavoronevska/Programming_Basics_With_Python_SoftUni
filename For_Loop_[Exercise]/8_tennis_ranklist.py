WIN_POINTS = 2000
FINAL_POINTS = 1200
SEMI_FINAL_POINTS = 720

tournaments = int(input())
starting_points = int(input())

final_points = 0
count_wins = 0

for _ in range(tournaments):
    stage = str(input())

    if stage == "W":
        count_wins += 1
        final_points += WIN_POINTS
    elif stage == "F":
        final_points += FINAL_POINTS
    elif stage == "SF":
        final_points += SEMI_FINAL_POINTS

total_points = starting_points + final_points

print(f"Final points: {total_points}")
print(f"Average points: {final_points // tournaments}")
print(f"{count_wins / tournaments * 100:.2f}%")