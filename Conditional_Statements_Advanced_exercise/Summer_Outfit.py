degrees = int(input())
time_of_the_day = input()

outfits = ""
shoes = ""

if time_of_the_day == "Morning":
    if 10 <= degrees <= 18:
        outfits = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < degrees <= 24:
        outfits = "Shirt"
        shoes = "Moccasins"
    else:
        outfits = "T-Shirt"
        shoes = "Sandals"

elif time_of_the_day == "Afternoon":
    if 10 <= degrees <= 18:
        outfits = "Shirt"
        shoes = "Moccasins"
    elif 18 < degrees <= 24:
        outfits = "T-Shirt"
        shoes = "Sandals"
    else:
        outfits = "Swim Suit"
        shoes = "Barefoot"

else:
    if 10 <= degrees <= 18:
        outfits = "Shirt"
        shoes = "Moccasins"
    elif 18 < degrees <= 24:
        outfits = "Shirt"
        shoes = "Moccasins"
    else:
        outfits = "Shirt"
        shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {outfits} and {shoes}.")
