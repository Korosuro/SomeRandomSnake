#Rock Paper Scissors game

import random

list = ["Schere", "Stein", "Papier"]
C = random.choice(list)
counter = 0

while counter < 50:
    U = str(input("Schere, Stein oder Papier? "))
    if C == U:
        counter += 1
        print (counter)
        print (C)
        print (U)
        print ("Draw!")
    elif C != U:
        if C == "Schere" and U == "Papier" or C == "Stein" and U == "Schere" or C == "Papier" and U == "Stein":
            counter += 1
            print (counter)
            print (C)
            print (U)       
            print ("Computer wins!")
        else:
            counter += 1
            print (counter)
            print (C)
            print (U)
            print ("User wins!")