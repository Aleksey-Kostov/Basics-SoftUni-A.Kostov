
poor_grade_count = int(input())

total_count_grade = 0
last_problem = ""
average_grade = 0
count_grade = 0
sum_grade = 0
name_task = ""
poor_count_grade = 0

while name_task != "Enough":
    name_task = input()
    if name_task == "Enough":
        print(f"Average score: {average_grade:.2f}")
        print(f"Number of problems: {total_count_grade}")
        print(f"Last problem: {last_problem}")
        break
    grade = int(input())
    total_count_grade += 1
    sum_grade += grade
    last_problem = name_task
    average_grade = sum_grade / total_count_grade
    if 2 <= grade <= 4:
        poor_count_grade += 1
        if poor_count_grade == poor_grade_count:
            print(f"You need a break, {poor_count_grade} poor grades.")
            break
