n = int(input())
counter = 0

for num_1 in range(n + 1):
    for num_2 in range(n + 1):
        for num_3 in range(n + 1):
            if num_1 + num_2 + num_3 == n:
                counter += 1
                break
print(counter)