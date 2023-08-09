hours_of_exam = int(input())
minutes_of_exam = int(input())
hours_of_arrival = int(input())
minutes_of_arrival = int(input())

diff_hours = (hours_of_exam - hours_of_arrival) * 60
diff_minutes = (minutes_of_exam - minutes_of_arrival)
total_diff = diff_hours + diff_minutes

if abs(total_diff) > 59:
    hours_diff = abs(total_diff) // 60
    minutes_diff = abs(total_diff) % 60
else:
    hours_diff = 0
    minutes_diff = abs(total_diff)

if total_diff < 0:
    print("Late")
    if hours_diff == 0 and minutes_diff <= 59:
        print(f"{minutes_diff} minutes after the start")
    else:
        print(f"{hours_diff:01d}:{minutes_diff:02d} hours after the start")
elif total_diff > 30:
    print("Early")
    if hours_diff == 0 and minutes_diff <= 59:
        print(f"{minutes_diff} minutes before the start")
    else:
        print(f"{hours_diff:01d}:{minutes_diff:02d} hours before the start")
elif 0 <= total_diff <= 30:
    print("On time")
    if hours_diff == 0 and 0 < minutes_diff <= 30:
        print(f"{minutes_diff} minutes before the start")
    else:
        print("")
