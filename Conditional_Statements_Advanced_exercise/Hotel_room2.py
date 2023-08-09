month = input()
days = int(input())

apartment_price = 0
studio_price = 0

if month == "May" or month == "October":
    apartment_price = 65
    studio_price = 50
    if 7 < days <= 14:
        studio_price *= 0.95
    elif days > 14:
        studio_price *= 0.70

elif month == "June" or month == "September":
    apartment_price = 68.70
    studio_price = 75.20
    if days > 14:
        studio_price *= 0.80

elif month == "July" or month == "August":
    apartment_price = 77
    studio_price = 76

if days > 14:
    apartment_price *= 0.9

print(f"Apartment: {apartment_price * days:.2f} lv.")
print(f"Studio: {studio_price * days:.2f} lv.")
