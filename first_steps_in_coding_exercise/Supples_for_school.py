pens_packs = int(input())
marker_packs = int(input())
liters_detergent = int(input())
discount = int(input()) / 100

PENS_PRICE = 5.8
MARKERS_PRICE = 7.2
DETERGENT_PRICE = 1.20

price_before_discount = \
    (pens_packs * PENS_PRICE) + \
    (marker_packs * MARKERS_PRICE) + \
    (liters_detergent * DETERGENT_PRICE)
total_price = price_before_discount - (price_before_discount * discount)

print(total_price)
