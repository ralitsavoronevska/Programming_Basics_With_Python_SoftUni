number_of_pairs = int(input())
sums = []

for number in range(number_of_pairs):
    first_number = int(input())
    second_number = int(input())

    current_sum = first_number + second_number
    sums.append(current_sum)

if all(x == sums[0] for x in sums):
    print(f"Yes, value={sums[0]}")
else:
    max_diff = 0
    for i in range(1, len(sums)):
        diff = abs(sums[i] - sums[i - 1])
        if diff > max_diff:
            max_diff = diff
    print(f"No, maxdiff={max_diff}")