number_of_dancers = int(input())
numbers_of_points = float(input())
season = input()
place = input()

total_points = 0

win_points = number_of_dancers * numbers_of_points

if place == "Abroad":
    win_points += win_points * 0.5
    if season == "summer":
        total_points = win_points - (win_points * 0.1)
    elif season == "winter":
        total_points = win_points - (win_points * 0.15)
elif place == "Bulgaria":
    win_points = win_points
    if season == "summer":
        total_points = win_points - (win_points * 0.05)
    elif season == "winter":
        total_points = win_points - (win_points * 0.08)

amount_for_charity = total_points * 0.75
free_money = total_points - amount_for_charity
money_for_dancers = free_money / number_of_dancers

print(f"Charity - {amount_for_charity:.2f}")
print(f"Money per dancer - {money_for_dancers:.2f}")
