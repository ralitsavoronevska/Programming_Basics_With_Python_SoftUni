men = int(input())
women = int(input())
tables = int(input())

couples_count = 0
couples_list = []

for man in range(1, men + 1):
    for woman in range(1, women + 1):
        if couples_count >= tables:
            break
        couple = f"({man} <-> {woman})"
        couples_list.append(couple)
        couples_count += 1

    if couples_count >= tables:
        break

print(" ".join(couples_list))