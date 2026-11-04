m = int(input())

passwords = []

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d:
                    if (a * b) + (c * d) == m:
                        passwords.append(f"{a}{b}{c}{d}")

if len(passwords) >= 0:
    print(" ".join(passwords))
    if len(passwords) >= 4:
        print(f"Password: {passwords[3]}")
    else:
        print("No!")
else:
    print("No!")