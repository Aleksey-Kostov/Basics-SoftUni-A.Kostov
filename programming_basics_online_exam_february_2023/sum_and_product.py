n = int(input())

Flag = False
count = 0

for a in range(1, 10):
    for b in range(9, a, - 1):
        for c in range(0, 10):
            for d in range(9, c, - 1):
                multiplication = a * b * c * d
                collect = a + b + c + d
                if multiplication // collect == 3 and n % 3 == 0:
                    count += 1
                    Flag = True
                    print(f"{d}{c}{b}{a}")
                    break
                elif multiplication == collect and n % 10 == 5:
                    count += 1
                    Flag = True
                    print(f"{a}{b}{c}{d}")
                    break
            if Flag:
                break
        if Flag:
            break
    if Flag:
        break
if count == 0:
    print("Nothing found")
