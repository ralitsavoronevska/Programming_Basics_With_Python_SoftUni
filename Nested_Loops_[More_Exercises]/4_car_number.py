start = int(input())
end = int(input())

special_number = 0
special_numbers = set()

for i in range(start, end+1):
    for j in range(start, end+1):
        for k in range(start, end+1):
            for l in range(start, end+1):
                starts_with_even_digit = False
                starts_with_odd_digit = False
                ends_with_even_digit = False
                ends_with_odd_digit = False
                first_digit_bigger_than_the_last = False
                sum_of_second_and_third_digits_is_an_even_number = False
                is_number_special = False

                if i % 2 == 0:
                    starts_with_even_digit = True
                else:
                    starts_with_odd_digit = True

                if (k + j) % 2 == 0:
                    sum_of_second_and_third_digits_is_an_even_number = True

                if l % 2 == 0:
                    ends_with_even_digit = True
                else:
                    ends_with_odd_digit = True

                if i > l:
                    first_digit_bigger_than_the_last = True

                if ((starts_with_even_digit and ends_with_odd_digit) or (starts_with_odd_digit and ends_with_even_digit)) and sum_of_second_and_third_digits_is_an_even_number and first_digit_bigger_than_the_last:
                    is_number_special = True
                    special_number = 1000 * i + 100 * j + 10 * k + l
                    special_numbers.add(special_number)

print(' '.join(map(str, sorted(special_numbers))))