junior_cyclists_count = int(input())
senior_cyclists_count = int(input())
track_type = input()

total_tax_junior = 0
total_tax_senior = 0

if junior_cyclists_count > 0:
    if track_type == "trail":
        total_tax_junior = junior_cyclists_count * 5.5
    elif track_type == "cross-country":
        total_tax_junior = junior_cyclists_count * 8
        if junior_cyclists_count >= 50:
            total_tax_junior = junior_cyclists_count * (8 * 0.75)
    elif track_type == "downhill":
        total_tax_junior = junior_cyclists_count * 12.25
    elif track_type == "road":
        total_tax_junior = junior_cyclists_count * 20

if senior_cyclists_count > 0:
    if track_type == "trail":
        total_tax_senior = senior_cyclists_count * 7
    elif track_type == "cross-country":
        total_tax_senior = senior_cyclists_count * 9.5
        if senior_cyclists_count >= 50:
            total_tax_senior = senior_cyclists_count * (9.5 * 0.75)
    elif track_type == "downhill":
        total_tax_senior = senior_cyclists_count * 13.75
    elif track_type == "road":
        total_tax_senior = senior_cyclists_count * 21.50

donation = total_tax_junior + total_tax_senior
donation *= 0.95

print(f"{donation:.2f}")
