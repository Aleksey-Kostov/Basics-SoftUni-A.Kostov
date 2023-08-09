target = 10000
total_foot = 0

while total_foot < target:
    foot = input()

    if foot == "Going home":
        foot = int(input())
        total_foot += foot
        break
    total_foot += int(foot)

if total_foot >= target:
    print(f"Goal reached! Good job!")
    print(f"{total_foot - target} steps over the goal!")
else:
    print(f"{target - total_foot} more steps to reach goal.")
