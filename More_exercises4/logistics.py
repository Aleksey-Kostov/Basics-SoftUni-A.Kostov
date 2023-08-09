cargo_number = int(input())

BUS = 200
TRACK = 175
TRAIN = 120

total_cargo_weight = 0
total_price = 0
total_price_train = 0
total_price_bus = 0
total_price_track = 0
average_weight = 0
cargo_weight_bus = 0
cargo_weight_track = 0
cargo_weight_train = 0

for _ in range(cargo_number):
    cargo_weight = float(input())
    total_cargo_weight += cargo_weight
    if 0 < cargo_weight <= 3:
        price_bus = cargo_weight * BUS
        total_price_bus += price_bus
        cargo_weight_bus += cargo_weight
    elif 4 <= cargo_weight <= 11:
        price_track = cargo_weight * TRACK
        total_price_track += price_track
        cargo_weight_track += cargo_weight
    else:
        price_train = cargo_weight * TRAIN
        total_price_train += price_train
        cargo_weight_train += cargo_weight
    average_weight = (total_price_train + total_price_bus + total_price_track) / total_cargo_weight

total_cargo_weight_bus = cargo_weight_bus / total_cargo_weight * 100
total_cargo_weight_track = cargo_weight_track / total_cargo_weight * 100
total_cargo_weight_train = cargo_weight_train / total_cargo_weight * 100

print(f"{average_weight:.2f}")
print(f"{total_cargo_weight_bus:.2f}%")
print(f"{total_cargo_weight_track:.2f}%")
print(f"{total_cargo_weight_train:.2f}%")
