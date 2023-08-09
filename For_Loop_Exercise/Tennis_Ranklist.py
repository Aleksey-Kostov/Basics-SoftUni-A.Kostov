from math import floor

number_of_tournaments = int(input())
starting_points = int(input())

current_points_1 = 0
current_points_2 = 0
current_points_3 = 0
win = 0

for i in range(number_of_tournaments):
    stage_reached = input()
    if stage_reached == "W":
        current_points_1 += 2000
        win += 1
    elif stage_reached == "F":
        current_points_2 += 1200
    elif stage_reached == "SF":
        current_points_3 += 720

total_points = current_points_1 + current_points_2 + current_points_3 + starting_points
average_points = (total_points - starting_points) / number_of_tournaments
number_of_winn = win / number_of_tournaments * 100

print(f"Final points: {total_points}")
print(f"Average points: {floor(average_points)}")
print(f"{number_of_winn:.2f}%")
