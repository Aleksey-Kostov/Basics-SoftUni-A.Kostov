number = int(input())
counter = 0

while True:
    current_num = int(input())
    counter += current_num
    if counter >= number:
        print(counter)
        break
