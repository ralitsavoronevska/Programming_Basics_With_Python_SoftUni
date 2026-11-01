n = int(input())

sum_first_two_nums = 0
sum_second_two_nums = 0
lucky_numbers = set()

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                sum_first_two_nums = i + j
                sum_second_two_nums = k + l
                if sum_first_two_nums == sum_second_two_nums and n % sum_first_two_nums == 0:
                    lucky_number = 1000 * i + 100 * j + 10 * k + l
                    lucky_numbers.add(lucky_number)

print(' '.join(map(str, sorted(lucky_numbers))))