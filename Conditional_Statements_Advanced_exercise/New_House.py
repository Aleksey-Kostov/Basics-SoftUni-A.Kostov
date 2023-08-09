type_of_the_flowers = input()
flowers_count = int(input())
budget = int(input())

ROSES_PRICE = 5
DAHLIAS_PRICE = 3.8
TULIPS_PRICE = 2.8
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.5

total_price = 0

if type_of_the_flowers == "Roses":
    total_price = ROSES_PRICE * flowers_count
    if flowers_count > 80:
        total_price *= 0.9
elif type_of_the_flowers == "Dahlias":
    total_price = DAHLIAS_PRICE * flowers_count
    if flowers_count > 90:
        total_price *= 0.85
elif type_of_the_flowers == "Tulips":
    total_price = TULIPS_PRICE * flowers_count
    if flowers_count > 80:
        total_price *= 0.85
elif type_of_the_flowers == "Narcissus":
    total_price = NARCISSUS_PRICE * flowers_count
    if flowers_count < 120:
        total_price *= 1.15
elif type_of_the_flowers == "Gladiolus":
    total_price = GLADIOLUS_PRICE * flowers_count
    if flowers_count < 80:
        total_price *= 1.20

if budget >= total_price:
    print(f"Hey, you have a great garden with {flowers_count} {type_of_the_flowers} and" 
          f" {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")
