import sys

number_elements = int(input())

max_element = -sys.maxsize
sum_elements = 0

for _ in range(number_elements):
    num = int(input())

    if num > max_element:
        max_element = num

    sum_elements += num

half_sum = sum_elements - max_element

if half_sum == max_element:
    print("Yes")
    print(f"Sum = {max_element}")
else:
    print("No")
    print(f"Diff = {abs(max_element - half_sum)}")