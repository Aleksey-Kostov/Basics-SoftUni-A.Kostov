price_of_kilogram_vegetable = float(input())
price_of_kilogram_fruit = float(input())
kilograms_for_vegetable = int(input())
kilograms_for_fruit = int(input())

EURO_COURSE = 1.94

all_price_in_bgn = (price_of_kilogram_vegetable * kilograms_for_vegetable) +\
                    (price_of_kilogram_fruit * kilograms_for_fruit)

all_price_in_EURO = all_price_in_bgn / EURO_COURSE

print(f"{all_price_in_EURO:.2f}")
