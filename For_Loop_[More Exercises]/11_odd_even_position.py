import sys

n = int(input())

odd_sum = 0
even_sum = 0
odd_list = []
even_list = []
odd_min_number = float("inf")
odd_max_number = float("-inf")
even_min_number = float("inf")
even_max_number = float("-inf")

for i in range(1, n + 1):
    number = float(input())

    if i % 2 == 0:
        even_sum += number
        even_list.append(number)
    else:
        odd_sum += number
        odd_list.append(number)

for i in range(len(even_list)):
    if even_list[i] < even_min_number:
        even_min_number = even_list[i]
    if even_list[i] > even_max_number:
        even_max_number = even_list[i]

for i in range(len(odd_list)):
    if odd_list[i] < odd_min_number:
        odd_min_number = odd_list[i]
    if odd_list[i] > odd_max_number:
        odd_max_number = odd_list[i]

print(f"OddSum={odd_sum:.2f},")

if odd_list:
    print(f"OddMin={odd_min_number:.2f},")
    print(f"OddMax={odd_max_number:.2f},")
else:
    print("OddMin=No,")
    print("OddMax=No,")

print(f"EvenSum={even_sum:.2f},")

if even_list:
    print(f"EvenMin={even_min_number:.2f},")
    print(f"EvenMax={even_max_number:.2f}")
else:
    print("EvenMin=No,")
    print("EvenMax=No")

