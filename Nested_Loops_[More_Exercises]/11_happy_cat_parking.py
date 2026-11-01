days = int(input())
hours = int(input())

total_tax = 0

for day in range(1, days + 1):
    tax_per_day = 0

    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            tax_per_day += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            tax_per_day += 1.25
        else:
            tax_per_day += 1.00
    total_tax += tax_per_day

    print(f"Day: {day} - {tax_per_day:.2f} leva")
print(f"Total: {total_tax:.2f} leva")