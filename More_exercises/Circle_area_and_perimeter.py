from math import pi

radius_r = float(input())

area_circle = radius_r ** 2 * pi
perimeter_circle = pi * 2 * radius_r

print(f"{area_circle:.2f}")
print(f"{perimeter_circle:.2f}")
