num1 = int(input())
num2 = int(input())

for numbers in range(num1, num2 + 1):
    numbers_to_str = str(numbers)
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(numbers_to_str):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if even_sum == odd_sum:
        print(numbers, end=" ")
