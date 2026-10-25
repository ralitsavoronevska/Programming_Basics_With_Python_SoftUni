students = int(input())
highest_grades_students = 0
high_grades_students = 0
medium_grades_students = 0
low_grades_students = 0
total_grades_sum = 0

for student in range(1, students + 1):
    grade = float(input())

    if 5.00 <= grade:
        highest_grades_students += 1
    if 4.00 <= grade <= 4.99:
        high_grades_students += 1
    if 3.00 <= grade <= 3.99:
        medium_grades_students += 1
    if 2.00 <= grade <= 2.99:
        low_grades_students += 1
    total_grades_sum += grade
highest_grades_average = highest_grades_students / students * 100
high_grades_average = high_grades_students / students * 100
medium_grades_average = medium_grades_students / students * 100
low_grades_average = low_grades_students / students * 100
grades_average = total_grades_sum / students

print(f"Top students: {highest_grades_average:.2f}%")
print(f"Between 4.00 and 4.99: {high_grades_average:.2f}%")
print(f"Between 3.00 and 3.99: {medium_grades_average:.2f}%")
print(f"Fail: {low_grades_average:.2f}%")
print(f"Average: {grades_average:.2f}")