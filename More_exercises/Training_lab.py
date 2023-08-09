w, h = float(input()) * 100, float(input()) * 100

CORRIDOR = 100
ONE_BUREAU = 70
ONE_ROW = 120
SEAT_FOR_CHAIR = 3

bureau_for_row = (h - CORRIDOR) // ONE_BUREAU
number_of_row = w // ONE_ROW

total_seats = (bureau_for_row * number_of_row) - SEAT_FOR_CHAIR

print(f"{total_seats:.0f}")
