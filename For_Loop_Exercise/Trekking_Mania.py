n = int(input())

num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0

for i in range(n):
    man_count = int(input())
    if man_count <= 5:
        num1 += man_count
    elif 5 < man_count <= 12:
        num2 += man_count
    elif 12 < man_count <= 25:
        num3 += man_count
    elif 25 < man_count <= 40:
        num4 += man_count
    elif man_count > 40:
        num5 += man_count

total = num1 + num2 + num3 + num4 + num5
percent_1 = (num1 / total) * 100
percent_2 = (num2 / total) * 100
percent_3 = (num3 / total) * 100
percent_4 = (num4 / total) * 100
percent_5 = (num5 / total) * 100

print(f"{percent_1:.2f}%")
print(f"{percent_2:.2f}%")
print(f"{percent_3:.2f}%")
print(f"{percent_4:.2f}%")
print(f"{percent_5:.2f}%")
