cinema_name = input()

cinema_count_student = 0
cinema_count_standard = 0
cinema_count_kid = 0
total_free_seat = 0
total_cinema_count = 0

student_seat = 0
standard_seat = 0
kid_seat = 0


while cinema_name != "Finish":
    free_seat = int(input())
    cinema_count = 0

    while cinema_count < free_seat:
        tipe_ticket = input()
        if tipe_ticket == "student":
            cinema_count_student += 1
        elif tipe_ticket == "standard":
            cinema_count_standard += 1
        elif tipe_ticket == "kid":
            cinema_count_kid += 1
        elif tipe_ticket == "End":
            break
        cinema_count += 1
    total_cinema_count += cinema_count
    kid_seat = cinema_count_kid / total_cinema_count * 100
    standard_seat = cinema_count_standard / total_cinema_count * 100
    student_seat = cinema_count_student / total_cinema_count * 100
    total_free_seat = cinema_count / free_seat * 100
    print(f"{cinema_name} - {total_free_seat:.2f}% full.")
    cinema_name = input()

print(f"Total tickets: {total_cinema_count}")
print(f"{student_seat:.2f}% student tickets.")
print(f"{standard_seat:.2f}% standard tickets.")
print(f"{kid_seat:.2f}% kids tickets.")

