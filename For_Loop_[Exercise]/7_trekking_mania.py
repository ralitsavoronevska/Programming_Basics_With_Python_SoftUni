groups = int(input())

count_people_musala = 0
count_people_monblan = 0
count_people_kilimandjaro = 0
count_people_k2 = 0
count_people_everest = 0

for _ in range(groups):
    people = int(input())

    if people <= 5:
        count_people_musala += people
    elif 6 <= people <= 12:
        count_people_monblan += people
    elif 13 <= people <= 25:
        count_people_kilimandjaro += people
    elif 26 <= people <= 40:
        count_people_k2 += people
    else:
        count_people_everest += people

total_people_count = (count_people_musala + count_people_monblan +
                      count_people_kilimandjaro + count_people_k2 + count_people_everest)

percent_people_musala = (count_people_musala / total_people_count) * 100
percent_people_monblan = (count_people_monblan / total_people_count) * 100
percent_people_kilimandjaro = (count_people_kilimandjaro / total_people_count) * 100
percent_people_k2 = (count_people_k2 / total_people_count) * 100
percent_people_everest = (count_people_everest / total_people_count) * 100

print(f"{percent_people_musala:.2f}%")
print(f"{percent_people_monblan:.2f}%")
print(f"{percent_people_kilimandjaro:.2f}%")
print(f"{percent_people_k2:.2f}%")
print(f"{percent_people_everest:.2f}%")