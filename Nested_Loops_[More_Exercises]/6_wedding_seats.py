last_sector = str(input())
rows_in_sector_a = int(input())
seats_odd_rows = int(input())
seats_count = 0

for i in range(ord("A"), ord(last_sector) + 1):
    rows = rows_in_sector_a + (i - ord("A"))
    for row in range(1, rows + 1):
        seats = 0

        if row % 2 != 0:
            seats += seats_odd_rows
        else:
            seats += seats_odd_rows + 2

        seats_count += seats

        for seat in range(0, seats):
            print(f"{chr(i)}{row}{chr(seat + ord('a'))}")

print(seats_count)