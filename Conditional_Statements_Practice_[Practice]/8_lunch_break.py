from math import ceil

name_of_series = str(input())
duration_of_series = int(input())
duration_of_lunch_break = int(input())

time_for_lunch = duration_of_lunch_break * 1/8
time_for_break = duration_of_lunch_break * 1/4

time_left_for_series = duration_of_lunch_break - time_for_lunch - time_for_break
time_diff = abs(time_left_for_series - duration_of_series)

if time_left_for_series >= duration_of_series:
    print(f"You have enough time to watch {name_of_series} and left with {ceil(time_diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_series}, you need {ceil(time_diff)} more minutes.")