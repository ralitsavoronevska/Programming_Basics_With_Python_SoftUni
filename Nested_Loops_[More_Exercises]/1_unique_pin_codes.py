upper_limit_first_number = int(input())
upper_limit_second_number = int(input())
upper_limit_third_number = int(input())

even_first_numbers = []
prime_second_numbers = []
even_third_numbers = []

for num in range(2, upper_limit_first_number + 1):
    if num % 2 == 0:
        even_first_numbers.append(num)

for num in range(2, upper_limit_second_number + 1):
    is_prime = True
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
            is_prime = False
            break
    if is_prime:
        prime_second_numbers.append(num)

for num in range(2, upper_limit_third_number + 1):
    if num % 2 == 0:
        even_third_numbers.append(num)

for first in even_first_numbers:
    for second in prime_second_numbers:
        for third in even_third_numbers:
            print(f"{first} {second} {third}")