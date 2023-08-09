period = int(input())

treated_patients = 0
untreated_patients = 0
DOCTORS = 7

for num in range(1, period + 1):
    patient_number = int(input())
    if num % 3 == 0:
        if treated_patients < untreated_patients:
            DOCTORS += 1
    if patient_number <= DOCTORS:
        treated_patients += patient_number
    else:
        treated_patients += DOCTORS
        untreated_patients += patient_number - DOCTORS

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
