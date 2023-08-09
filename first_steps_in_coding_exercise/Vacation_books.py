numbers_of_page = int(input())
page_for_hours = int(input())
numbers_of_days = int(input())

all_time_read_book = numbers_of_page // page_for_hours
hours_for_day = all_time_read_book // numbers_of_days

print(hours_for_day)
