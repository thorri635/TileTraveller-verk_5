location = (1,1)

while location != (3,1):
    if location == (1,1):
        print("You can travel: (N)orth.")
        the_way = input("Direction:")
        if the_way == "N" or the_way == "n":
            location = (1,2)
        else:
            print("Not a valid direction!")
    elif location == (1,2):
        print("You can travel: (N)orth or (E)ast or (S)outh")
        the_way = input("Direction:")
        if the_way == "N" or the_way == "n":
            location = (1,3)
        elif the_way == "E" or the_way == "e":
            location = (2,2)
        elif the_way == "S" or the_way == "s":
            location = (1,1)
        else:
            print("Not a valid direction!")
    elif loaction == (1,3):
        print("You can travel: (E)ast or (S)outh")

        print("Thorri u are a god damn faget")
