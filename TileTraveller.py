location = (1,1)

while location != (3,1):
    if location == (1,1):
        print("You can travel: (N)orth.")
        the_way = input("Direction:")
        if the_way == "N" or the_way == "n":
            location = (1,2)
        else:
            print("Not a valid direction!")
    if location == (1,2):
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
    if location == (1,3):
        print("You can travel: (E)ast or (S)outh")
<<<<<<< HEAD
        the_way = input("Direction")
        if the_way == 'E' or the_way =='e':
            location = (2,3)
        elif the_way =='S' or the_way == 's':
            location =(1,2)
        else:
            print("Not a valid direction!")
    if location == (2,3):
        print("You can travel: (E)ast or (W)est")
        the_way = input("Direction:")
        if the_way == 'E' or the_way =='e':
            location = (3,3)
        elif the_way =='W' or the_way =='w':
            location = (1,3)
        else:
            print("Not a valid direction!")
    if location == (3,3):
        print('You can travel: (E)ast or (S)outh')
        the_way= input('Direction:')
        if the_way =='E' or the_way =='e':
            location = (2,3)
        elif the_way =='S' or the_way =='s':
            location = (3,2)
        else:
            print('Not a valid directon!')
    if location ==(3,2):
        print('You can travel: (N)orth or (S)outh')
        the_way= input('Direction:')
        if the_way =='N' or the_way =='n':
            location =(3,3)
        elif the_way =='S' or the_way =='s':
            location = (3,1)
        else:
            print('Not a valid direction!')
    if location ==(2,2):
        print('You can travel: (W)est or (S)outh')
        the_way = input('Direction:')
        if the_way =='W' or the_way =='w':
            location = (1,2)
        elif the_way =='S' or the_way =='s':
            location = (2,1)
        else:
            print('Not a valid direction!')
    if location ==(2,1):
        print('You can travel: (N)orth')
        if the_way =='N' or the_way =='n':
            location = (2,2)
        else:
            print('Not a valid direction!')    

if location ==(3,1):
    print('Victory')
=======

        print("Thorri u are a god damn faget")
>>>>>>> 0e2ea3cb253e3976e11571ad2519425d72eb73b2
