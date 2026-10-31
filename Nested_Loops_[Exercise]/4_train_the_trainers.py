judges = int(input())

total_sum_grades = 0
total_count = 0

while True:
    presentation_name = str(input())

    if presentation_name == "Finish":
        break

    current_sum_grades = 0

    for _ in range(judges):
        grade = float(input())
        current_sum_grades += grade

    print(f"{presentation_name} - {current_sum_grades / judges:.2f}.")
    total_sum_grades += current_sum_grades
    total_count += judges

print(f"Student's final assessment is {total_sum_grades / total_count:.2f}.")