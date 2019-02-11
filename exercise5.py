move = input("Would you like to walk or run? (enter 'go home' to stop) ")
distance = 0

while move == "walk" or move == "run":
    if move == "walk":
        distance += 1
        print("You are {}km from home".format(distance))
        move = input("Would you like to walk or run? ")
    elif move == "run":
        distance += 5
        print("You are {}km from home".format(distance))
        move = input("Would you like to walk or run? ")
    elif move == "go home":
        print("You are {}km from home".format(distance))
        print("Time to head home!")
