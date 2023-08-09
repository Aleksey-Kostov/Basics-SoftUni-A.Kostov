fuel_type = input("")
liters_fuel = float(input())
club_card = input("")

total_price = 0

GASOLINE = 2.22
DIESEL = 2.33
GAS = 0.93

if fuel_type == "Gasoline":
    total_price = liters_fuel * GASOLINE
    if club_card == "Yes":
        total_price = (GASOLINE - 0.18) * liters_fuel
    if 20 <= liters_fuel <= 25:
        total_price -= total_price * 0.08
    elif liters_fuel > 25:
        total_price -= total_price * 0.10

if fuel_type == "Diesel":
    total_price = liters_fuel * DIESEL
    if club_card == "Yes":
        total_price = (DIESEL - 0.12) * liters_fuel
    if 20 <= liters_fuel <= 25:
        total_price -= total_price * 0.08
    elif liters_fuel > 25:
        total_price -= total_price * 0.10

if fuel_type == "Gas":
    total_price = liters_fuel * GAS
    if club_card == "Yes":
        total_price = (GAS - 0.08) * liters_fuel
    if 20 <= liters_fuel <= 25:
        total_price -= total_price * 0.08
    elif liters_fuel > 25:
        total_price -= total_price * 0.10

print(f"{total_price:.2f} lv.")
