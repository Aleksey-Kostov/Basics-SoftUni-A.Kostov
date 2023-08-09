from math import ceil

serial_name = input("")
episode_duration = int(input())
lunch_break_duration = int(input())

time_lunch = lunch_break_duration / 8
time_recreation = lunch_break_duration / 4

time_left = lunch_break_duration - (time_lunch + time_recreation)

if time_left >= episode_duration:
    print(f"You have enough time to watch"
          f" {serial_name} and left with"
          f" {ceil(time_left - episode_duration)}"
          f" minutes free time.")
else:
    print(f"You don't have enough time to watch"
          f" {serial_name}, you need"
          f" {ceil(episode_duration - time_left)}"
          f" more minutes.")
