n = int(input())
firs_line = 0
second_line = 0

for i in range(2 * n):
    numbers = int(input())
    if i < n:
        firs_line += numbers
    else:
        second_line += numbers

if firs_line == second_line:
    print(f"Yes, sum = {abs(firs_line)}")
else:
    print(f"No, diff = {abs(firs_line - second_line)}")
