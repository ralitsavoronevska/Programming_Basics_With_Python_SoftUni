number_in_range = int(input())
result = ""

if (-100 <= number_in_range <= 100) and (number_in_range != 0):
    result = "Yes"
else:
    result = "No"

print(result)