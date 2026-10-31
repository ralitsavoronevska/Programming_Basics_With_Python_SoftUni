rows = int(input())

counter = 0
is_max_number = False

for row in range(1, rows + 1):
    for _ in range(row):
        counter += 1
        print(counter, end=' ')

        if counter == rows:
            is_max_number = True
            break
    if is_max_number:
        break
    print()