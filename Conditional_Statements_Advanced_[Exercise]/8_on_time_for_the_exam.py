MINUTES_IN_ONE_HOUR = 60

exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time = (exam_hour * MINUTES_IN_ONE_HOUR) + exam_minutes
arrival_time = (arrival_hour * MINUTES_IN_ONE_HOUR) + arrival_minutes
time_diff = exam_time - arrival_time

if time_diff < 0:
    print("Late")
elif time_diff > 30:
    print("Early")
else:
    print("On time")

hours = abs(time_diff) // MINUTES_IN_ONE_HOUR
minutes = abs(time_diff) % MINUTES_IN_ONE_HOUR

result = ""

if hours > 0:
    result += f"{hours}:{minutes:02d} hours"
elif minutes > 0:
    result += f"{minutes} minutes"

if time_diff > 0:
    result += " before the start"
elif time_diff < 0:
    result += " after the start"
print(result)
