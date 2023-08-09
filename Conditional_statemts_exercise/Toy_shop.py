excursion_price = float(input())
puzzle_count = int(input())
talking_dolls_count = int(input())
flushed_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

PUZZLE_PRICE = 2.60
TALKING_DOLLS_PRICE = 3
FLUSHED_BEARS_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2

total_toys_count = puzzle_count + \
                   talking_dolls_count + \
                   flushed_bears_count + \
                   minions_count + \
                   trucks_count

total_price_toys = (puzzle_count * PUZZLE_PRICE) + \
                   (talking_dolls_count * TALKING_DOLLS_PRICE) + \
                   (flushed_bears_count * FLUSHED_BEARS_PRICE) + \
                   (minions_count * MINION_PRICE) + \
                   (trucks_count * TRUCK_PRICE)

if total_toys_count >= 50:
    total_price_toys *= 0.75

total_price_toys *= 0.9

if total_price_toys >= excursion_price:
    print(f"Yes! {total_price_toys - excursion_price:.2f} lv left.")
else:
    print(f"Not enough money! {excursion_price - total_price_toys:.2f} lv needed.")
