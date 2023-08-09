deposit = float(input())
term_of_the_deposit = int(input())
annual_interest_rate = float(input()) / 100

accrued_interest = deposit * annual_interest_rate
monthly_interest = accrued_interest / 12
total = deposit + (term_of_the_deposit * monthly_interest)

print(total)
