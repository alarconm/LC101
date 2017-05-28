# Xprompt user for integer input for how many games should be played
# Xdefine user input can only be odd numbers
# Xmake it best of format ie 3 out of 5, 2 out of 3, etc.
# X human player prompt rock paper or scissors
# X capture human players input into variable
# X computer randomly chooses one of 3 options out of rock paper or scissors
# X display match result human vs computer
# display the current number of wins for each player
# X variable for number of wins each player
# X if tie occurs, redo that match and don't count it as played
# X determine how many to do


import random


def main():

    human = 0
    computer = 0
    howmany = int(input("Best of how many games? Has to be an odd number and not over 9.\n"))

    if howmany > 9 or howmany % 2 == 0:
        print("Did you even read the directions? Try again.\n")
        main()

        score = ''

    for each in range(howmany):
        score = rockpaperscissors()

        while score == "tie":
            score = rockpaperscissors()
        if score == "human":
            human += 1
        elif score == "computer":
            computer += 1
        print("Round", each + 1, "Human:", human, "Computer:", computer,"\n")

        if human > howmany / 2 or computer > howmany / 2:
           break

    print("Final score Human:", human, "Computer:", computer)


def rockpaperscissors():
    """get input to to determine rock/paper/scissors, generate choice for computer
    check to see who wins computer or human then send score"""

    human = int(input("For rock, choose 1. For paper, choose 2. For scissors, choose 3.\n"))
    computer = random.randrange(1,4)

    if human == computer:
        print ("Tie - replay\n")
        return "tie"

    if human == 1 and computer == 2:
        print ("Computer chose paper - you lose\n")
        return "computer"

    if human == 1 and computer == 3:
        print ("Computer chose scissors - you win!\n")
        return "human"

    if human == 2 and computer == 3:
        print ("Computer chose scissors - you lose!\n")
        return "computer"

    if human == 2 and computer == 1:
        print ("Computer chose rock - you win!\n")
        return "human"

    if human == 3 and computer == 2:
        print ("Computer chose paper - you win!\n")
        return "human"

    if human == 3 and computer == 1:
        print ("Computer chose rock - you lose!\n")
        return "computer"


main()
