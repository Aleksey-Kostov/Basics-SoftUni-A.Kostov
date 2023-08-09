age = int(input())
price_washing_machine = float(input())
toys_price = int(input())

sum_money = 10
sum_toys = 0
money_given = 0

for num in range(1, age+1):
    if num % 2 == 0:
        money_given += sum_money - 1
        sum_money += 10
    else:
        sum_toys += toys_price

total_sum = money_given + sum_toys

if total_sum >= price_washing_machine:
    print(f"Yes! {total_sum - price_washing_machine:.2f}")
else:
    print(f"No! {price_washing_machine - total_sum:.2f}")
