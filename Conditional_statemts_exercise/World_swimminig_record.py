record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds = float(input())

RESISTANCE_TIME = 12.5
RESISTANCE_DISTANCE = 15

time_for_swimming = distance_in_meters * time_in_seconds
time_resistance = (distance_in_meters // RESISTANCE_DISTANCE) * RESISTANCE_TIME
total_time = time_for_swimming + time_resistance

if total_time >= record_in_seconds:
    print(f"No, he failed! He was {total_time - record_in_seconds:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
