name = input()

grade_count = 1
poor_grade = 0
total_grade = 0
average_grade = 0

while True:
    if poor_grade > 1:
        print(f"{name} has been excluded at {grade_count} grade")
        break
    grade = float(input())
    if 4 <= grade <= 6:
        total_grade += grade
        average_grade = total_grade / grade_count
        if grade_count == 12:
            print(f"{name} graduated. Average grade: {average_grade:.2f}")
            break
        grade_count += 1
    elif 2 <= grade < 4:
        poor_grade += 1
