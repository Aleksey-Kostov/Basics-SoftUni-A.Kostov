n = int(input())
salary = int(input())

for _ in range(n):
    site = input()
    if site == "Facebook":
        salary -= 150
    elif site == "Instagram":
        salary -= 100
    elif site == "Reddit":
        salary -= 50
    else:
        salary = salary
    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(salary)
