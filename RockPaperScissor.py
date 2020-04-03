# Rock, Paper, Scissors Game
# Make a rock-paper-scissors game where it is the player vs the computer.
# The computer’s answer will be randomly generated, while the program will ask the user for their input.
# This project will better your understanding of while loops and if statements.

import random

print("Welcome To \"Rock Paper Scissor\" Game.")

round = 1
tryAgain = True
choices = ("Rock", "Paper", "Scissor")
computerPickRandomizer = int(random.randrange(0, 3))
computerPick = (choices[computerPickRandomizer]).lower()

while tryAgain:
    while round >= 1:
        playerPicking = input("Please select your Choice(Rock, Paper, Scissor): ").lower()
        if playerPicking == "rock":
            if computerPick == "rock":
                print("Draw")
                computerPickRandomizer = int(random.randrange(0, 3))
                computerPick = (choices[computerPickRandomizer]).lower()
            elif computerPick == "paper":
                print("Computer Wins!")
                break
            elif computerPick == "scissor":
                print("Player Wins!")
                break

        elif playerPicking == "paper":
            if computerPick == "rock":
                print("Player Wins!")
                break
            elif computerPick == "paper":
                print("Draw!")
                computerPickRandomizer = int(random.randrange(0, 3))
                computerPick = (choices[computerPickRandomizer]).lower()
            elif computerPick == "scissor":
                print("Computer Wins!")
                break

        elif playerPicking == "scissor":
            if computerPick == "rock":
                print("Computer Wins!")
                break
            elif computerPick == "paper":
                print("Player Wins!")
                break
            elif computerPick == "scissor":
                print("Draw!")
                computerPickRandomizer = int(random.randrange(0, 3))
                computerPick = (choices[computerPickRandomizer]).lower()
        else:
            print("Please Select a valid input")
        round += 1
    playerTryAgain = input("Try Again (Y)?").lower()
    if playerTryAgain == "y":
        tryAgain = True
        computerPickRandomizer = int(random.randrange(0, 3))
        computerPick = (choices[computerPickRandomizer]).lower()
    else:
        tryAgain = False
