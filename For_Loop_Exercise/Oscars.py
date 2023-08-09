name_of_actor = input()
total_score = float(input())
number_of_assessors = int(input())

for _ in range(number_of_assessors):
    name_of_assessor = input()
    points_from_assessor = float(input())
    number_of_letters = len(name_of_assessor)
    current_points = (points_from_assessor * number_of_letters) / 2
    total_score += current_points
    if total_score >= 1250:
        break

if total_score >= 1250:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_score:.1f}!")

else:
    print(f"Sorry, {name_of_actor} you need {(1250.5 - total_score):.1f} more!")
