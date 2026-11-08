locations_count = int(input())

for location in range(locations_count):
    total_gold_extracted = 0
    expected_average_daily_gold_yield = float(input())
    digging_days = int(input())
    for day in range(digging_days):
        gold_extracted_for_the_day = float(input())
        total_gold_extracted += gold_extracted_for_the_day
    average_daily_gold_yield = total_gold_extracted / digging_days

    if average_daily_gold_yield >= expected_average_daily_gold_yield:
        print(f"Good job! Average gold per day: {average_daily_gold_yield:.2f}.")
    else:
        print(f"You need {expected_average_daily_gold_yield - average_daily_gold_yield:.2f} gold.")