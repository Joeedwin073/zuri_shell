from random import choice
import random

list = ["R","P","S"]

print("""
    *****Welcome to Rock, Paper and Scissors Python game*****
            Make a choice amongst the following
                    R for Rock
                    P for Paper
                    S for Scissors
            You have a maximum of 5 choices to make

                    let's gooo.....
""")

for i in range(0,5):
    resp = input("What is your choice? ")
    comp = random.choice(list)
    if resp == comp:
        print("Oh you guessed the same as the other player... Try again.")
        if comp == "R":
            print("Player(Rock): Computer(Rock)")
        elif comp == "S":
            print("Player(Scissors): Computer(Scissors)")
        elif comp == "P":
            print("Player(Paper): Computer(Paper)")
        pass
    elif resp == "R" and comp == "S":
        print("You won!!! ")
        print("Player(Rock) : Computer(Scissors)")
        break
    elif resp == "S" and comp == "P":
        print("You won!!! ")
        print("Player(Scissors) : Computer(Paper)")
        break
    elif resp == "P" and comp == "R":
        print("You won!!! ")
        print("Player(Paper) : Computer(Scissors)")
        break
    elif resp == "R" and comp == "P":
        print("You Lost!!! ")
        print("Player(Rock): Computer(Paper)")
        break

    elif comp == "R" and resp == "S":
        print("You Lost!!! ")
        print("Computer(Rock) : Player(Scissors)")
        break
    elif comp == "S" and resp == "P":
        print("You Lost!!! ")
        print("Computer(Scissors) : Player(Paper)")
        break
    elif comp == "P" and resp == "S":
        print("You Lost!!! ")
        print("Computer(Paper) : Player(Scissors)")
        break
    else:
        print("You have not selected a valid option! ")
        pass
    i = i + 1

Print("Thank you for playing... ")



# Things to do for the task ahead

# first inform them about the game

# then take user input

# check if it is a valid input 

# check if it is the same as the computer random function

# if it is the same then there is a tie, loop it
 
# if not then check the progression and detect the winners