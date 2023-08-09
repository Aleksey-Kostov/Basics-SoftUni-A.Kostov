goal_for_the_day = int(input())

mens = 15
ladies = 20
kids = 10
touch_up = 20
full_color = 30

current_goal = 0

while current_goal < goal_for_the_day:
    data = input()
    if data == "closed":
        break
    if data == "haircut" or data == "mens" or data == "ladies" or data == "kids":
        if data == "mens":
            current_goal += mens
        elif data == "ladies":
            current_goal += ladies
        elif data == "kids":
            current_goal += kids
    if data == "color" or data == "touch up" or data == "full color":
        if data == "touch up":
            current_goal += touch_up
        elif data == "full color":
            current_goal += full_color

if current_goal >= goal_for_the_day:
    print(f"You have reached your target for the day!")
else:
    print(f"Target not reached! You need {goal_for_the_day - current_goal}lv. more.")

print(f"Earned money: {current_goal}lv.")
