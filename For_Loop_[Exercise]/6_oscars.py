MIN_POINTS = 1250.5

actor_name = str(input())
academy_points = float(input())
judges = int(input())

is_nominee = False

for _ in range(judges):
    judge_name = str(input())
    judge_points = float(input())

    academy_points += (len(judge_name) * judge_points / 2)

    if academy_points > MIN_POINTS:
        is_nominee = True
        break

if is_nominee:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {MIN_POINTS - academy_points:.1f} more!")