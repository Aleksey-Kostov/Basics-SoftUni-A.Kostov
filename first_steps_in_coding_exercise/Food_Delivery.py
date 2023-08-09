numbers_of_chicken_menus = int(input())
numbers_of_fish_menus = int(input())
numbers_of_vegetarian_menus = int(input())

PRICE_CHICKEN_MENUS = 10.35
PRICE_FISH_MENUS = 12.40
PRICE_VEGETARIAN_MENUS = 8.15
PRICE_DELIVERY = 2.50

menus_price =\
    (numbers_of_chicken_menus * PRICE_CHICKEN_MENUS) +\
    (numbers_of_fish_menus * PRICE_FISH_MENUS) +\
    (numbers_of_vegetarian_menus * PRICE_VEGETARIAN_MENUS)

desert_price = menus_price * 0.20

total_menu_order = desert_price + menus_price + PRICE_DELIVERY

print(f"{total_menu_order:.2f}")
