book_pages = int(input())
pages_per_hour = int(input())
total_days = int(input())

total_hours = book_pages // pages_per_hour
needed_hours_per_day = total_hours // total_days

print(needed_hours_per_day)