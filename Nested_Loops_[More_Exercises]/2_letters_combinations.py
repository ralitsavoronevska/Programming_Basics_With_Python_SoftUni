start = input()
end = input()
exclude = input()

combinations = 0
result = []

for i in range(ord(start), ord(end) + 1):
    for j in range(ord(start), ord(end) + 1):
        for k in range(ord(start), ord(end) + 1):
            combination = chr(i) + chr(j) + chr(k)
            if exclude not in combination:
                result.append(combination)
                combinations += 1

print(" ".join(result), combinations)