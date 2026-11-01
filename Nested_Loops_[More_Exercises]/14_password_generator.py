n = int(input())
l = int(input())

passwords = []

for num_1 in range(1, n + 1):
    for num_2 in range(1, n + 1):
        for letter_1 in range(97, 97 + l):
            for letter_2 in range(97, 97 + l):
                for num_3 in range(1, n + 1):
                    if num_3 > num_1 and num_3 > num_2:
                        passwords.append(f"{num_1}{num_2}{chr(letter_1)}{chr(letter_2)}{num_3}")
print(" ".join(passwords))