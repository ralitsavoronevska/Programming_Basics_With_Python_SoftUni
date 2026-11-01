a = int(input())
b = int(input())
max_number_generated_passwords = int(input())

A = 35
B = 64
passwords_count = 0

for x in range(1, a + 1):
    for y in range(1, b + 1):

        if passwords_count >= max_number_generated_passwords:
            break

        print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")

        passwords_count += 1

        A += 1
        B += 1

        if A > 55:
            A = 35

        if B > 96:
            B = 64

    if passwords_count >= max_number_generated_passwords:
        break