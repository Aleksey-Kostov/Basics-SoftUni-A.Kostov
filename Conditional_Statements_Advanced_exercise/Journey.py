budget = float(input())
season = input()

place_of_rest = None
destination = None

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        budget *= 0.3
        place_of_rest = "Camp"
    elif season == "winter":
        budget *= 0.7
        place_of_rest = "Hotel"

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        budget *= 0.4
        place_of_rest = "Camp"
    elif season == "winter":
        budget *= 0.8
        place_of_rest = "Hotel"

else:
    destination = "Europe"
    if season == "summer" or season == "winter":
        budget *= 0.9
        place_of_rest = "Hotel"

print(f"Somewhere in {destination}")
print(f"{place_of_rest} - {budget:.2f}")
