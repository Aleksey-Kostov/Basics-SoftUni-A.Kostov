money_for_excursion = int(input())
money_on_hand = float(input())

spend_money = 0
save_money = 0
days_spent = 0
total_days = 0
secret_word = False

while money_on_hand <= money_for_excursion and days_spent < 5:
    text = input()
    money = float(input())
    total_days += 1
    if text == "spend":
        days_spent += 1
        spend_money = money_on_hand - money
        if days_spent == 5:
            secret_word = True
            break
    elif text == "save":
        days_spent = 0
        save_money = spend_money + money
        if save_money >= money_for_excursion:
            break
        elif spend_money < 0:
            save_money = 0 + money
            if save_money >= money_for_excursion:
                break

if days_spent == 5 and secret_word:
    print(f"You can't save the money.")
    print(total_days)
else:
    print(f"You saved the money for {total_days} days.")
