day_tournament = int(input())

day_count = 0
count_win = 0
count_lose = 0
total_money = 0
total_win = 0
total_lose = 0


while day_tournament > day_count:

    text = input()
    current_win = 0
    current_lose = 0
    won_money = 0
    while text != "Finish":
        text = input()
        if text == "win":
            current_win += 1
            won_money += 20
            count_win += 1
        elif text == "lose":
            current_lose += 1
            count_lose += 1
        elif text == "Finish":
            day_count += 1
    if current_win > current_lose:
        won_money *= 1.1
    total_money += won_money


if count_win > count_lose:
    total_money *= 1.20

if count_win > count_lose:
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
