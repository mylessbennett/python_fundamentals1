move = input("Would you like to walk or run? (s to stop) ")
distance = 0

while move == "walk" or move == "run":
    if move == "walk":
        distance += 1
        move = input("Would you like to walk or run? ")
    elif move == "run":
        distance += 5
        move = input("Would you like to walk or run? ")

    print("You are {}km from home".format(distance))
