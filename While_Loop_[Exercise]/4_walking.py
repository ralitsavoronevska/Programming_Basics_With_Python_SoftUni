DAILY_GOAL_IN_STEPS = 10000

steps = 0

while steps < DAILY_GOAL_IN_STEPS:
    command = input()

    if command == "Going home":
        steps_to_home = int(input())
        steps += steps_to_home
        break
    else:
        steps += int(command)

if steps >= DAILY_GOAL_IN_STEPS:
    print("Goal reached! Good job!")
    print(f"{steps - DAILY_GOAL_IN_STEPS} steps over the goal!")
else:
    print(f"{DAILY_GOAL_IN_STEPS - steps} more steps to reach goal.")