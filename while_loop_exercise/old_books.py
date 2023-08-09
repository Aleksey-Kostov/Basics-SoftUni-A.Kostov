name_book = input()

variable_name = str

book_count = -1

while variable_name != name_book:
    variable_name = input()
    book_count += 1
    if variable_name == name_book:
        print(f"You checked {book_count} books and found it.")
    elif variable_name == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {book_count} books.")
        break
