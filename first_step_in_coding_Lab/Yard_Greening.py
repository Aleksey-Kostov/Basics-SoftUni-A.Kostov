square_meters = float(input())

PRICE = float(7.61)

all_price = square_meters * PRICE
discount = all_price * float(0.18)
final_price = (all_price - discount)

print(final_price)
print(discount)