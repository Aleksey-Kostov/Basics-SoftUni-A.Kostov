n = int(input())

even = 0
odd = 0

for num in range(n):
    numbers = int(input())
    if num % 2 == 0:
        even += numbers
    else:
        odd += numbers

if even == odd:
    print(f"Yes\nSum = {even}")
else:
    print(f"No\nDiff = {abs(odd - even)}")
