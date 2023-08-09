import sys
line = input()
max_number = - sys.maxsize

while line != "Stop":
    numbers = int(line)
    if numbers > max_number:
        max_number = numbers
    line = input()
print(max_number)
