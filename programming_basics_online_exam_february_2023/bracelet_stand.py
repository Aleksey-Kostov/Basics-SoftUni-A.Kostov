pocket_money = float(input())
money_from_sales = float(input())
expenses = float(input())
price_of_gift = float(input())

DAYS = 5

total_packet_money = pocket_money * DAYS
total_money_from_sales = money_from_sales * DAYS
total_money = (total_packet_money + total_money_from_sales) - expenses

if total_money >= price_of_gift:
    print(f"Profit: {total_money:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {(price_of_gift - total_money):.2f} BGN.")
