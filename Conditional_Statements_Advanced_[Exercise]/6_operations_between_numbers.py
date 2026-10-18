n1 = int(input())
n2 = int(input())
operator = str(input())
result = 0
type_of_number = ""

if operator == '+':
    result = n1 + n2
elif operator == '-':
    result = n1 - n2
elif operator == '*':
    result = n1 * n2
elif n2 == 0:
    print(f"Cannot divide {n1} by zero")
    exit()
elif operator == '/':
    result = n1 / n2
elif operator == '%':
    result = n1 % n2

if operator == '+' or operator == '-' or operator == '*':
    if result % 2 == 0:
        type_of_number = "even"
    else:
        type_of_number = "odd"
    print(f"{n1} {operator} {n2} = {result} - {type_of_number}")
elif operator == '/':
    print(f"{n1} / {n2} = {result:.2f}")
elif operator == '%':
    print(f"{n1} % {n2} = {result}")