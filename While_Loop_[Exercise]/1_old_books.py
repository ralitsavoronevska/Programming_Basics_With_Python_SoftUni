title_of_book = str(input())
checked_books = 0
book_is_found = False

while True:
    random_book = str(input())

    if random_book == "No More Books":
        break
    elif random_book != title_of_book:
        checked_books += 1
        continue
    else:
        book_is_found = True
        break

if book_is_found:
    print(f"You checked {checked_books} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {checked_books} books.")