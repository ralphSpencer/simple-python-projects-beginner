# Guess The Number
# Write a programme where the computer randomly generates a number between 0 and 20.
# The user needs to guess what the number is.
# If the user guesses wrong, tell them their guess is either too high, or too low.

import random  # import random module
print("Welcome to \"Guess the Number\".")  # title of the game

randAnswer = random.randrange(0,20)  # system selects a number for user to guess
guessTry = 1  # initialized starting point of loop

while guessTry >= 1:  # until guessTry is not 0 or a negative number the loop will continue
    userGuess = int(input("\nSelect a number from 0-20: "))  # ask input from the user
    if userGuess >= 0 & userGuess <= 20:  # checks if user input is not greater that 20 or lower than 0
        if userGuess != randAnswer:  # if guess is incorrect
            if userGuess > randAnswer+3:  # if the guess is too far from the answer
                print("Number is Too High")
            elif userGuess >= randAnswer+1:  # if the guess is closer but higher from the answer
                print("Number is High")
            elif userGuess < randAnswer-3:  # if the guess is too low from the answer
                print("Number is Too Low")
            elif userGuess <= randAnswer-1:  # if the guess is closer but lower from the answer
                print("Number is Low")
        elif userGuess == randAnswer:  # if the answer is correct
            print("You are correct")
            break  # breaks the loop
    else:  # if the guess is greater than 20 or lower than 0
        print("Please select a number from 0-20 only \n")
    guessTry += 1

print("The answer is " + str(randAnswer))  # shows the answer
