number_1 = int(input())
number_2 = int(input())
operator = input()

result = 0

if operator == "+":
    result = f"{number_1} + {number_2} = {number_1 + number_2}" +\
             (" - even" if (number_1 + number_2) % 2 == 0 else " - odd")

elif operator == "-":
    result = f"{number_1} - {number_2} = {number_1 - number_2}" +\
             (" - even" if (number_1 - number_2) % 2 == 0 else " - odd")

elif operator == "*":
    result = f"{number_1} * {number_2} = {number_1 * number_2}" + \
             (" - even" if (number_1 * number_2) % 2 == 0 else " - odd")

elif number_2 == 0:
    result = f"Cannot divide {number_1} by zero"

elif operator == "%":
    result = f"{number_1} % {number_2} = {number_1 % number_2}"

elif operator == "/":
    result = f"{number_1} / {number_2} = {number_1 / number_2:.2f}"

print(result)
