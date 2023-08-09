budget_film = float(input())
numbers_extras = int(input())
price_clothing = float(input())

film_decor = budget_film * 0.1
total_price_clothing = price_clothing * numbers_extras

if numbers_extras >= 150:
    total_price_clothing *= 0.9

if (film_decor + total_price_clothing) > budget_film:
    print("Not enough money!")
    print(f"Wingard needs {film_decor + total_price_clothing - budget_film:.2f} leva more.")
elif (film_decor + total_price_clothing) <= budget_film:
    print("Action!")
    print(f"Wingard starts filming with {budget_film - film_decor - total_price_clothing:.2f} leva left.")
