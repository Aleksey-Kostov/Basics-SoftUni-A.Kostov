number_of_trainers = int(input())

theme_count = 0
total_evaluation = 0
average_evaluation = 0

while True:
    theme = input()
    theme_count += 1
    if theme == "Finish":
        print(f"Student's final assessment is {average_evaluation:.2f}.")
        break
    data_count = 0
    current_average_evaluation = 0
    evaluation = 0
    while data_count < number_of_trainers:
        data = input()
        data_count += 1
        evaluation += float(data)
        current_average_evaluation = evaluation / number_of_trainers
        if data_count == number_of_trainers:
            print(f"{theme} - {current_average_evaluation:.2f}.")
    total_evaluation += current_average_evaluation
    average_evaluation = total_evaluation / theme_count

