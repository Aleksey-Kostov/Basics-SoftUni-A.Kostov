from math import ceil

numbers_of_days = int(input())
kilometers = float(input())

current_kilometers = kilometers
all_kilometers = 0

for _ in range(numbers_of_days):
    percent_norm = int(input())
    kilometers += (kilometers * percent_norm)/100
    all_kilometers += kilometers

total_kilometers = all_kilometers + current_kilometers

if all_kilometers >= 1000:
    print(f"You've done a great job running {ceil(total_kilometers - 1000)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(1000 - total_kilometers)} more kilometers")
