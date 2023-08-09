budget = float(input())
category_of_ticket = input()
man_count = int(input())

VIP_TICKET = 499.99
NORMAL_TICKET = 249.99

price_transport = 0
price_vip_ticket = VIP_TICKET * man_count
price_normal_ticket = NORMAL_TICKET * man_count

if 1 <= man_count <= 4:
    price_transport = budget * 0.75
elif 5 <= man_count <= 9:
    price_transport = budget * 0.60
elif 10 <= man_count <= 24:
    price_transport = budget * 0.50
elif 25 <= man_count <= 49:
    price_transport = budget * 0.40
else:
    price_transport = budget * 0.25

total_price_1 = price_transport + price_vip_ticket
total_price_2 = price_transport + price_normal_ticket

if category_of_ticket == "VIP":
    if total_price_1 > budget:
        print(f"Not enough money! You need {total_price_1 - budget:.2f} leva.")
    else:
        print(f"Yes! You have {budget - total_price_1:.2f} leva left.")
else:
    if total_price_2 > budget:
        print(f"Not enough money! You need {total_price_2 - budget:.2f} leva.")
    else:
        print(f"Yes! You have {budget - total_price_2:.2f} leva left.")
