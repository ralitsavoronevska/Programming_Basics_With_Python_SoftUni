ROOM_FOR_ONE_PERSON = 18.00
APARTMENT = 25.00
PRESIDENT_APARTMENT = 35.00

days_of_stay = int(input())
type_of_premises = str(input())
rating = str(input())
nights_of_stay = days_of_stay - 1
discount = 0
price = 0
total_price = 0

if type_of_premises == 'room for one person':
    price = nights_of_stay * ROOM_FOR_ONE_PERSON
elif type_of_premises == 'apartment':
    if nights_of_stay > 15:
        discount = 0.5
    elif 10 <= nights_of_stay <= 15:
        discount = 0.35
    elif nights_of_stay < 10:
        discount = 0.3
    price = nights_of_stay * APARTMENT
elif type_of_premises == 'president apartment':
    if nights_of_stay > 15:
        discount = 0.2
    elif 10 <= nights_of_stay <= 15:
        discount = 0.15
    elif nights_of_stay < 10:
        discount = 0.10
    price = nights_of_stay * PRESIDENT_APARTMENT
total_price = price - (price * discount)

if rating == "positive":
    total_price += total_price * 0.25
elif rating == "negative":
    total_price -= total_price * 0.1

print(f"{total_price:.2f}")