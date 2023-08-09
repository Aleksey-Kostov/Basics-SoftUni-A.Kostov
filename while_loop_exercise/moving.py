width = int(input())
distance = int(input())
depth = int(input())

volume_room = width * distance * depth

total_cubic_meters = 0

while total_cubic_meters <= volume_room:
    carton_volume = input()
    if carton_volume == "Done":
        break
    total_cubic_meters += int(carton_volume)

if total_cubic_meters >= volume_room:
    print(f"No more free space! You need {total_cubic_meters - volume_room} Cubic meters more.")
else:
    print(f"{volume_room - total_cubic_meters} Cubic meters left.")