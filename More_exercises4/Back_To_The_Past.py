money_inheritance = float(input())
years_lives = int(input())

years = 18
even_year_spending = 12000

for num in range(1800, years_lives + 1):
    if num % 2 == 0:
        money_inheritance -= even_year_spending
    elif num % 2 != 0:
        money_inheritance -= (even_year_spending + 50 * years)
    years += 1

if money_inheritance >= 0:
    print(f"Yes! He will live a carefree life and will have {money_inheritance:.2f} dollars left.")
else:
    print(f"He will need {abs(money_inheritance):.2f} dollars to survive.")

