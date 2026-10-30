student = str(input())
grade = 1
sum_of_marks = 0
max_tries = 0

while True:
    yearly_mark = float(input())

    if yearly_mark < 4.00:
        max_tries += 1

        if max_tries > 1:
            print(f"{student} has been excluded at {grade} grade")
            break
        continue

    sum_of_marks += yearly_mark
    if grade == 12:
        avrg_grade = sum_of_marks / 12
        print(f"{student} graduated. Average grade: {avrg_grade:.2f}")
        break
    grade += 1