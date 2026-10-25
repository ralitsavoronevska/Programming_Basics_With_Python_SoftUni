inheritance_amount = float(input())
year_upper_limit = int(input())
year_lower_limit = 1800
amount_spent = 0
even_sum = 12000


for idx in range(year_lower_limit, year_upper_limit + 1):
    age = 18 + (idx - 1800)

    if idx % 2 == 0:
        amount_spent += even_sum
    else:
        amount_spent += 12000 + 50 * age

if inheritance_amount < amount_spent:
    print(f"He will need {amount_spent - inheritance_amount:.2f} dollars to survive.")
else:
    print(f"Yes! He will live a carefree life and will have {inheritance_amount - amount_spent:.2f} dollars left.")