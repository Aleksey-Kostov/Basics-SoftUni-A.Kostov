length = int(input())
width = int(input())

number_of_pieces = length * width

while number_of_pieces > 0:
    piece = input()
    if piece == "STOP":
        print(f"{number_of_pieces} pieces are left.")
        break
    cake = int(piece)
    number_of_pieces -= cake
    if number_of_pieces <= 0:
        print(f"No more cake left! You need {abs(number_of_pieces)} pieces more.")
