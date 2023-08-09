kilometers = int(input())
word = input("")

best_price = 0

TAXI_PRICE_FOR_KILOMETERS_DAY = 0.79
TAXI_PRICE_FOR_KILOMETERS_NIGHT = 0.90
TAXI_PRICE_FIRST = 0.70
BUS_FOR_KILOMETERS = 0.09
TRAIN_FOR_KILOMETERS = 0.06

if kilometers < 20 and word == "day":
    best_price = TAXI_PRICE_FIRST + kilometers * TAXI_PRICE_FOR_KILOMETERS_DAY
elif kilometers < 20 and word == "night":
    best_price = TAXI_PRICE_FIRST + kilometers * TAXI_PRICE_FOR_KILOMETERS_NIGHT
elif 20 <= kilometers < 100:
    best_price = kilometers * BUS_FOR_KILOMETERS
else:
    best_price = kilometers * TRAIN_FOR_KILOMETERS

print(f"{best_price:.2f}")
