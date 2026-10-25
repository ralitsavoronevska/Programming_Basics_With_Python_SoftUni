period = int(input())

doctors = 7
treated_patients = 0
untreated_patients = 0

for day in range(1, period + 1):
    patients = int(input())

    if day % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1

    daily_capacity = doctors
    treated_today = min(patients, daily_capacity)

    treated_patients += treated_today
    untreated_patients += patients - treated_today

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")