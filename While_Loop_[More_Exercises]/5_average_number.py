number_elements = int(input())

total = 0
index = 0

while index < number_elements:
    number = int(input())
    total += number
    index += 1

average = total / index
print(f"{average:.2f}")