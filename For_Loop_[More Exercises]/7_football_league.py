stadium_capacity = int(input())
fans = int(input())

sector_a_fans = 0
sector_b_fans = 0
sector_v_fans = 0
sector_g_fans = 0

for fan in range(1, fans + 1):
    sector = str(input())

    if sector == "A":
        sector_a_fans += 1
    if sector == "B":
        sector_b_fans += 1
    if sector == "V":
        sector_v_fans += 1
    if sector == "G":
        sector_g_fans += 1

sector_a_fans_percentage = sector_a_fans / fans * 100
sector_b_fans_percentage = sector_b_fans / fans * 100
sector_v_fans_percentage = sector_v_fans / fans * 100
sector_g_fans_percentage = sector_g_fans / fans * 100
total_fans = sector_a_fans + sector_b_fans + sector_v_fans + sector_g_fans
fans_percentage = total_fans / stadium_capacity * 100

print(f"{sector_a_fans_percentage:.2f}%")
print(f"{sector_b_fans_percentage:.2f}%")
print(f"{sector_v_fans_percentage:.2f}%")
print(f"{sector_g_fans_percentage:.2f}%")
print(f"{fans_percentage:.2f}%")
