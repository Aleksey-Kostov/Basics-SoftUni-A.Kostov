from math import ceil, floor

day_count = int(input())
food_lef_behind = int(input())
food_for_dog = float(input())
food_for_cat = float(input())
food_for_turtle = float(input())

needed_food_for_dog = day_count * food_for_dog
needed_food_for_cat = day_count * food_for_cat
needed_food_for_turtle = day_count * (food_for_turtle / 1000)

total_food = needed_food_for_turtle + needed_food_for_dog + needed_food_for_cat
difference = abs(food_lef_behind - total_food)

if food_lef_behind >= total_food:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f"{ceil(difference)} more kilos of food are needed.")
