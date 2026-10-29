count = int(input())

count_p1 = 0
count_p2 = 0
count_p3 = 0
count_p4 = 0
count_p5 = 0

for _ in range(count):
    num = int(input())

    if num < 200:
        count_p1 += 1
    elif 200<= num <= 399:
        count_p2 += 1
    elif 400 <= num <= 599:
        count_p3 += 1
    elif 600 <= num <= 799:
        count_p4 += 1
    else:
        count_p5 += 1

percent_p1 = count_p1 / count * 100
percent_p2 = count_p2 / count * 100
percent_p3 = count_p3 / count * 100
percent_p4 = count_p4 / count * 100
percent_p5 = count_p5 / count * 100

print(f"{percent_p1:.2f}%")
print(f"{percent_p2:.2f}%")
print(f"{percent_p3:.2f}%")
print(f"{percent_p4:.2f}%")
print(f"{percent_p5:.2f}%")