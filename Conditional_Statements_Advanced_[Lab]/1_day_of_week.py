day_of_the_week = int(input())
result = ""

if day_of_the_week == 1:
    result = "Monday"
elif day_of_the_week == 2:
    result = "Tuesday"
elif day_of_the_week == 3:
    result = "Wednesday"
elif day_of_the_week == 4:
    result = "Thursday"
elif day_of_the_week == 5:
    result = "Friday"
elif day_of_the_week == 6:
    result = "Saturday"
elif day_of_the_week == 7:
    result = "Sunday"
else:
    result = "Error"

print(result)