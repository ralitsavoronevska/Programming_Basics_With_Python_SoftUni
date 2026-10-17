norm_of_play_per_year_in_minutes = 30000
norm_of_play_per_day_on_a_working_day = 63
norm_of_play_per_day_on_on_off_day = 127
days_per_year = 365

off_days_in_a_year = int(input())

working_days_in_a_year = days_per_year - off_days_in_a_year
actual_play_time = (working_days_in_a_year * norm_of_play_per_day_on_a_working_day) + (off_days_in_a_year * norm_of_play_per_day_on_on_off_day)
diff = abs(norm_of_play_per_year_in_minutes - actual_play_time)
diff_in_hours = diff // 60
diff_in_minutes = diff % 60

if actual_play_time > norm_of_play_per_year_in_minutes:
    print("Tom will run away")
    print(f"{diff_in_hours} hours and {diff_in_minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{diff_in_hours} hours and {diff_in_minutes} minutes less for play")