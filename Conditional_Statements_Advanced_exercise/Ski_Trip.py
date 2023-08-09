day_of_stay = int(input())
type_of_stay = input()
rating = input()

PRICE_ROOM_FOR_ONE_PERSON = 18.00
PRICE_APARTMENT = 25.00
PRICE_PRESIDENT_APARTMENT = 35.00

nights_count = day_of_stay - 1
total_price_1 = nights_count * PRICE_ROOM_FOR_ONE_PERSON
total_price_2 = nights_count * PRICE_APARTMENT
total_price_3 = nights_count * PRICE_PRESIDENT_APARTMENT

if type_of_stay == "apartment":
    if day_of_stay < 10:
        total_price_2 *= 0.70
    elif 10 <= day_of_stay <= 15:
        total_price_2 *= 0.65
    else:
        total_price_2 *= 0.50
elif type_of_stay == "president apartment":
    if day_of_stay < 10:
        total_price_3 *= 0.90
    elif 10 <= day_of_stay <= 15:
        total_price_3 *= 0.85
    else:
        total_price_3 *= 0.80
else:
    total_price_1 = total_price_1

if rating == "positive":
    total_price_1 *= 1.25
    total_price_2 *= 1.25
    total_price_3 *= 1.25
    if type_of_stay == "apartment":
        print(f"{total_price_2:.2f}")
    elif type_of_stay == "president apartment":
        print(f"{total_price_3:.2f}")
    else:
        print(f"{total_price_1:.2f}")
else:
    total_price_1 *= 0.9
    total_price_2 *= 0.9
    total_price_3 *= 0.9
    if type_of_stay == "apartment":
        print(f"{total_price_2:.2f}")
    elif type_of_stay == "president apartment":
        print(f"{total_price_3:.2f}")
    else:
        print(f"{total_price_1:.2f}")
