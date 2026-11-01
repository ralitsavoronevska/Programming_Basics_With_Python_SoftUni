upper_limit_hundreds = int(input())
upper_limit_tens = int(input())
upper_limit_ones = int(input())

for i in range(2, upper_limit_hundreds + 1, 2):
    for j in range(2, upper_limit_tens + 1, 1):
        if j in [2, 3, 5, 7]:
            for k in range(2, upper_limit_ones + 1, 2):
                print(f"{i} {j} {k}")