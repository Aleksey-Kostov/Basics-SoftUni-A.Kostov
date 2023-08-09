from math import floor
from math import ceil

area_vineyard = int(input())
one_sq_m_vineyard = float(input())
liters_vine = int(input())
workers_count = int(input())

FOR_ONE_LITERS_VINE = 2.5

total_vineyard = area_vineyard * one_sq_m_vineyard
total_vine = (0.4 * total_vineyard) / FOR_ONE_LITERS_VINE
difference = abs(liters_vine - total_vine)
liters_for_every_worker = abs(difference / workers_count)

if liters_vine <= total_vine:
    print(f"Good harvest this year! Total wine: {floor(total_vine)} liters.")
    print(f"{ceil(difference)} liters left -> "
          f"{ceil(liters_for_every_worker)} liters per person.")
else:
    print(f"It will be a tough winter! More "
          f"{floor(difference)} liters wine needed.")
