holidays_count = int(input())

PLAY_WHEN_HI_IS_WORKING = 63
PLAY_WHEN_HI_IS_RELAXING = 127
ONE_YEARS = 365
NORM_FOR_YEARS = 30000

working_days = ONE_YEARS - holidays_count
real_time_for_playing = (working_days * PLAY_WHEN_HI_IS_WORKING) +\
                        (holidays_count * PLAY_WHEN_HI_IS_RELAXING)

difference = abs(NORM_FOR_YEARS - real_time_for_playing)
real_time_hours = difference // 60
real_time_minutes = difference % 60

if real_time_for_playing > NORM_FOR_YEARS:
    print("Tom will run away")
    print(f"{real_time_hours} hours and {real_time_minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{real_time_hours} hours and {real_time_minutes} minutes less for play")
