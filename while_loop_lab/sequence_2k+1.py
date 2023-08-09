num = int(input())

counter = 1

while True:
    print(counter)
    counter = counter * 2 + 1
    if counter > num:
        break
