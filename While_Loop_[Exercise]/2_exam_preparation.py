allowed_number_bad_grades = int(input())

sum_grades = 0
number_solved_problems = 0
current_bad_grades = 0
last_task_name = ""

while allowed_number_bad_grades > current_bad_grades:
    task_name = str(input())

    if task_name == "Enough":
        print(f"Average score: {sum_grades / number_solved_problems:.2f}")
        print(f"Number of problems: {number_solved_problems}")
        print(f"Last problem: {last_task_name}")
        break

    grade = int(input())

    if grade <= 4:
        current_bad_grades += 1

    sum_grades += grade
    number_solved_problems += 1
    last_task_name = task_name
else:
    print(f"You need a break, {current_bad_grades} poor grades.")