annual_fee = int(input())

shoes_price = annual_fee - (annual_fee * 0.40)
team_price = shoes_price - (shoes_price * 0.20)
ball_price = team_price / 4
accessories_price = ball_price / 5

total_expenses = annual_fee + shoes_price + team_price + ball_price + accessories_price

print(total_expenses)
