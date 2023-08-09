from math import floor, ceil

magnolias_count = int(input())
hyacinth_count = int(input())
roses_count = int(input())
cactus_count = int(input())
gift_price = float(input())

MAGNOLIAS_PRICE = 3.25
HYACINTH_PRICE = 4
ROSES_PRICE = 3.5
CACTUS_PRICE = 8

total_price = (magnolias_count * MAGNOLIAS_PRICE) +\
              (hyacinth_count * HYACINTH_PRICE) +\
              (roses_count * ROSES_PRICE) +\
              (cactus_count * CACTUS_PRICE)

total_price -= total_price * 0.05
difference = abs(total_price - gift_price)

if total_price >= gift_price:
    print(f"She is left with {floor(difference)} leva.")
else:
    print(f"She will have to borrow {ceil(difference)} leva.")
