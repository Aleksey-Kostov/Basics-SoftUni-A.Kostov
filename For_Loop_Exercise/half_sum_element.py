import sys
n = int(input())

total_number = 0
max_number = - sys.maxsize

for _ in range(n):
    number = int(input())
    total_number += number
    if number > max_number:
        max_number = number

remaining_numbers = total_number - max_number

if remaining_numbers == max_number:
    print(f"Yes\nSum = {remaining_numbers}")
else:
    print(f"No\nDiff = {abs(remaining_numbers - max_number)}")
