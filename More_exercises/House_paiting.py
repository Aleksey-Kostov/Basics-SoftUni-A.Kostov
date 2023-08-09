x = float(input())
y = float(input())
h = float(input())

GREEN_PAINT_SQ_M = 3.40
RED_PAINT_SQ_M = 4.30
WINDOWS_SIDE = 1.50
DOOR_X = 1.20
DOOR_Y = 2

area_side_wall = x * y
area_windows = WINDOWS_SIDE ** 2
area_both_side = (2 * area_side_wall) - (2 * area_windows)
rear_side = x ** 2
area_door = DOOR_Y * DOOR_X
area_rears_side = 2 * rear_side - area_door
total_area_green = area_both_side + area_rears_side
total_green_paint = total_area_green / GREEN_PAINT_SQ_M

rectangular_roofs = 2 * x * y
triangular_roof = ((x * h) / 2) * 2
total_area_red = rectangular_roofs + triangular_roof
total_red_paint = total_area_red / RED_PAINT_SQ_M

print(f"{total_green_paint:.2f}")
print(f"{total_red_paint:.2f}")
