from math import pi
figures = input("")
area = 0

if figures == "square":
    side = float(input())
    area = side ** 2
elif figures == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_b * side_a
elif figures == "circle":
    r = float(input())
    area = r ** 2 * pi
elif figures == "triangle":
    a = float(input())
    ha = float(input())
    area = a * ha / 2

print(f"{area:.3f}")
