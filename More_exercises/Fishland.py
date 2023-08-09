price_of_mackerel = float(input())
price_of_sprinkle = float(input())
kilograms_bonito = float(input())
kilograms_scad = float(input())
kilograms_mussels = int(input())

price_of_bonito = (price_of_mackerel + (price_of_mackerel * 0.6)) * kilograms_bonito
price_of_scad = (price_of_sprinkle + (price_of_sprinkle * 0.8)) * kilograms_scad
price_of_mussels = kilograms_mussels * 7.5

total_bill = price_of_bonito +\
             price_of_scad +\
             price_of_mussels

print(f"{total_bill:.2f}")
