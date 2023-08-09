length, width, height = int(input()), int(input()), int(input())
percent = float(input()) / 100

volume_tank = (length * width * height) / 1000
volume_tank -= volume_tank * percent

print(volume_tank)
