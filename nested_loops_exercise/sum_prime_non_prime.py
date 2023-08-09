
prime_numbers_sum = 0
non_prime_numbers_sum = 0
while True:
    numbers = input()

    if numbers == "stop":
        break

    current_number = int(numbers)
    if current_number < 0:
        print(f"Number is negative.")
        continue
    for i in range(2, current_number):
        if current_number % i == 0:
            break
    else:
        prime_numbers_sum += current_number
        continue
    non_prime_numbers_sum += current_number

print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {non_prime_numbers_sum}")
