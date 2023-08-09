import sys
line = input()
min_number = sys.maxsize

while line != "Stop":
    numbers = int(line)
    if numbers < min_number:
        min_number = numbers
    line = input()
print(min_number)
