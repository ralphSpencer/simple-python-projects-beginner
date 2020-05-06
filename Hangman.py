import random as rnd


def main_menu():
    print("\n\nWelcome to Hangman")
    print("""g
    1 - Start Game
    2 - Instruction
    3 - Quit Game
    """)
    # menu option input
    menu_choice = int(input("Select option: "))
    if menu_choice == 1:
        start_game()
    elif menu_choice == 2:
        game_instruction()
    elif menu_choice == 3:
        quit()
    else:
        print("Invalid option")


def start_game():
    word_list = ['Apricot', 'Brainstorm', 'Council', 'Danger', 'Sprite', 'Royalty', 'Ranger', 'Comics', 'Hotdog', 'Modem']
    word_num = rnd.randrange(0,10)
    word = word_list[word_num]
    word_letters = list(word.lower())

    player_guess = []
    player_lives = 6
    correct_guess = 0

    is_finished = False
    # show how many letter the word contain
    show_word = ["_" for x in word]
    for x in show_word:
        print(x, end=' ')
    # loops the game
    while is_finished is not True:
        # check if the player still has lives left
        if player_lives == 0:
            print('\nYou ran out of lives!')
            print('''
            _______
            |/   |    
            |   (_)    
            |   /|\          
            |    |        
            |   / \        
            |              
            |___     
            The word was ''' + word)
            is_finished = True
        elif player_lives > 0:
            # prompt user to select a letter
            player_answer = input('\nSelect a Letter: ')
            if player_answer in player_guess:
                print('Letter already selected!')
            else:
                player_guess.append(player_answer.lower())

                # outputs all the letter you have guessed
                for letters in word_letters:
                    if letters in player_guess:
                        answer = letters
                        print(letters, end=' ')
                    else:
                        answer = '_'
                        print('_', end=' ')
                # check if the letter is correct or wrong
                if player_answer in word_letters:
                    print('\nCorrect')
                    correct_guess += 1
                else:
                    print('\nWrong')
                    player_lives -= 1

                print('\nAnswers: ')
                for guess in player_guess:
                    print(guess.lower() + ' ', end=' ')

                if correct_guess == len(set(word_letters)):
                    is_finished = True
                    print("\nYou have guessed the word!"
                          "\nThe word was " + word)


def game_instruction():
    print("""\n\n
    How to play the game.
    
    The computer will think of a word.
    The player must guest the letter 
    of the word one at a time.
    The player has 6 lives before the
    he loses the game.
    Every wrong guess of letter will 
    remove a life.
    
    Good Luck and Have fun!
    
    1 - Start Game
    2 - Return to Menu
    3 - Quit Game
    """)
    menu_choice = int(input("Select option: "))
    if menu_choice == 1:
        start_game()
    elif menu_choice == 2:
        main_menu()
    elif menu_choice == 3:
        quit()
    else:
        print('Invalid Option')


def main():
    main_menu()


if __name__ == '__main__':
    main()