username = input()
password = input()
data = input()

while True:
    if data != password:
        data = input()
    else:
        print(f"Welcome {username}!")
        break
