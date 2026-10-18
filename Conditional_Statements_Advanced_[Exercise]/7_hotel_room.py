STUDIO_MAY_OCTOBER_PRICE = 50
STUDIO_JUNE_SEPTEMBER_PRICE = 75.20
STUDIO_JULY_AUGUST = 76

APARTMENT_MAY_OCTOBER_PRICE = 65
APARTMENT_JUNE_SEPTEMBER_PRICE = 68.70
APARTMENT_JULY_AUGUST = 77

month = str(input())
nights = int(input())
studio_amount = 0
apartment_amount = 0

if month == 'May' or month == 'October':
    studio_amount = nights * STUDIO_MAY_OCTOBER_PRICE
    apartment_amount = nights * APARTMENT_MAY_OCTOBER_PRICE
    if nights > 14:
        studio_amount -= studio_amount * 0.3
    elif nights > 7:
        studio_amount -= studio_amount * 0.05
elif month == 'June' or month == 'September':
    studio_amount = nights * STUDIO_JUNE_SEPTEMBER_PRICE
    apartment_amount = nights * APARTMENT_JUNE_SEPTEMBER_PRICE
    if nights > 14:
        studio_amount -= studio_amount * 0.2
elif month == 'July' or month == 'August':
    studio_amount = nights * STUDIO_JULY_AUGUST
    apartment_amount = nights * APARTMENT_JULY_AUGUST
if nights > 14:
    apartment_amount -= apartment_amount * 0.1

print(f"Apartment: {apartment_amount:.2f} lv.")
print(f"Studio: {studio_amount:.2f} lv.")