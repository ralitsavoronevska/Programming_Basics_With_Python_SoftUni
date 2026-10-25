time_period = int(input())
water_bill = 20
internet_bill = 15

electricity_bill_total = 0
water_bill_total = 0
internet_bill_total = 0
other_bills_total = 0

for month in range(1, time_period + 1):
    electricity_bill = float(input())

    electricity_bill_total += electricity_bill
    water_bill_total += water_bill
    internet_bill_total += internet_bill
    other_bills = electricity_bill + water_bill + internet_bill
    other_bills_total += other_bills * 1.2

average_bills_per_month = (electricity_bill_total + water_bill_total + internet_bill_total + other_bills_total) / time_period

print(f"Electricity: {electricity_bill_total:.2f} lv")
print(f"Water: {water_bill_total:.2f} lv")
print(f"Internet: {internet_bill_total:.2f} lv")
print(f"Other: {other_bills_total:.2f} lv")
print(f"Average: {average_bills_per_month:.2f} lv")