months = input()
number_of_nights = int(input())

total_price_1 = 0
total_price_2 = 0
place_1 = "Apartment"
place_2 = "Studio"

if months == "May" or months == "October":
    if place_2 == "Studio":
        total_price_1 = number_of_nights * 50
        if 7 < number_of_nights <= 14:
            total_price_1 = (50 - (50 * 0.05)) * number_of_nights
        elif number_of_nights > 14:
            total_price_1 = (50 - (50 * 0.30)) * number_of_nights
    if place_1 == "Apartment":
        total_price_2 = number_of_nights * 65
        if number_of_nights > 14:
            total_price_2 = (65 - (65 * 0.10)) * number_of_nights

if months == "June" or months == "September":
    if place_2 == "Studio":
        total_price_1 = number_of_nights * 75.20
        if number_of_nights > 14:
            total_price_1 = 75.20 - (75.20 * 0.20) * number_of_nights
    if place_1 == "Apartment":
        total_price_2 = number_of_nights * 68.70
        if number_of_nights > 14:
            total_price_2 = (68.70 - (68.70 * 0.10)) * number_of_nights

if months == "July" or months == "August":
    total_price_1 = number_of_nights * 76
    total_price_2 = number_of_nights * 77
    if number_of_nights > 14:
        total_price_2 = (77 - (77 * 0.10)) * number_of_nights


print(f"Apartment: {total_price_2:.2f} lv.")
print(f"Studio: {total_price_1:.2f} lv.")
