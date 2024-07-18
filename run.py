import random
import os
from wordlist import word_list
from wordlist import levels_list

# Functions to print colored text


def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))


def prRed(skk): print("\033[91m {}\033[00m" .format(skk))


def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))


def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))


"""
Get the name of the new player
"""


def get_name():
    os.system('clear')
    print("\n")
    prYellow("LET'S PLAY A GAME OF HANGMAN.\n")
    prCyan(" Hangman ".center(30, "*"))
    prRed("""
        -----------
        |         |
        |         |
        |
        |
        |
        |
        |

""")
    prCyan("*"*30)
    valid_name = False
    while not valid_name:
        new_name = input("Please enter your name:  ").capitalize()
        if bool(new_name) and not new_name.isnumeric():
            if new_name.replace(" ", "").isalnum() \
                    or new_name.replace("-", "").isalnum():
                valid_name = True
            else:
                prYellow("You didn't enter a valid name.")
                prYellow("You must enter a valid name to continue.")
        else:
            prYellow("You didn't enter a valid name.")
            prYellow("You must enter a valid name to continue.")
    return new_name


"""
Message to new player
"""


def intro_message():
    os.system('clear')
    print("\n")
    print("Hello, " + name + ".")
    prCyan("Here is how to play.")
    prCyan("Guess the letters or the whole word.")
    prCyan("If you make six wrong guesses, you lose!\n")
    choose_word()


"""
Choose a word difficulty and a random
word from the corresponding list
"""


def choose_word():
    print("What level of difficulty would you like to play?\n")
    prCyan(" Hangman ".center(30, "*"))
    print("""
        -----------
        |         |
        |         |
        |
        |   1 = EASY
        |   2 = INTERMEDIATE
        |   3 = DIFFICULT
        |
        |
        |
""")
    prCyan("*"*30)
    valid_choice = False
    while not valid_choice:
        difficulty = \
            input("\nEnter 1, 2 or 3 to choose a level of difficulty.")
        print(difficulty)
        if difficulty.isnumeric():
            choice = int(difficulty) - 1
            if choice < 0 or choice > 2:
                prYellow("Invalid. Your entry was not a 1, 2 or 3.   ")
            else:
                valid_choice = True
        else:
            prYellow("Invalid. Your entry was not a number.")
    word = random.choice(word_list[choice]).upper()
    print(word)
    os.system('clear')
    print("Let's begin!\n")
    play_game(word, choice)


"""
Message to continuing player
"""


def continue_message():
    os.system('clear')
    print("Hello again, " + name.capitalize() + ".")
    prCyan("Let's review how to play.")
    prCyan("Guess the letters or the whole word.")
    prCyan("If you make six wrong guesses, you lose!\n")
    choose_word()


"""
Play game
"""


def play_game(word, choice):
    # Convert word into a list of its letters
    word_letters = list(word)

    # Create list of correct letters in word with no
    # duplicates in order to compare to guessed letters list
    correct_letters = list(dict.fromkeys(word_letters))

    # Calculate number of letters in word
    num_of_letters = len(word)

    # Create a list for number positions of letters that match word
    positions = [x for x in range(num_of_letters)]

    # Create a string of dashes for each letter in word
    word_string = ["_" for x in range(num_of_letters)]
    display_wordstring = " ".join(word_string)

    # Create lists for guesses and variable for attempts
    guessed_letters = []
    guessed_words = []
    guessed_correct_letters = []
    attempts = 0

    # Create variable for puzzle not solved
    won = False

    # Create empty message that will be populated
    # as the player plays
    message = ""

    while not won and attempts < 6:
        # Create variable for player's guess and
        # print messages and outcomes
        prCyan("PLAYER: " + name.capitalize() + "  |  LEVEL: "
               + levels_list[choice])
        prCyan("*" * 40)
        print(display_hangman(attempts))
        prCyan("*" * 40)
        print("Letters already chosen: ")
        print(guessed_letters)
        prCyan("The word you're trying to guess has " +
               str(num_of_letters) + " letters.")
        prCyan(" " + display_wordstring + "\n")
        prYellow(message)
        guess = input("Please guess a letter or a word.").upper()
        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                os.system('clear')
                message = "You already guessed the letter " + guess + "."
            elif guess not in word:
                os.system('clear')
                message = "Incorrect! There's no '" + guess + "' in the word."
                guessed_letters.append(guess)
                attempts += 1
            else:
                os.system('clear')
                message = "Correct! " + guess + " is in the word."
                guessed_letters.append(guess)
                guessed_correct_letters.append(guess)
                for position, letter in zip(positions, word_letters):
                    if word_letters[position] == guess:
                        word_string[position] = guess
                        display_wordstring = " ".join(word_string)
                # Test if word is complete
                guessed_correct_letters.sort()
                correct_letters.sort()
                if guessed_correct_letters == correct_letters:
                    won = True
        elif guess.isalpha() and len(guess) > 1:
            if guess in guessed_words:
                message = "/nYou already guessed this word."
            elif guess == word.upper():
                message = "Congrats! Your word guess is correct!"
                won = True
            else:
                os.system('clear')
                message = guess + " is incorrect, please try again."
                guessed_words.append(guess)
                attempts += 1
        else:
            os.system('clear')
            message = "Oops! '" + guess + "' is not a valid guess, \
                please try again.\n"
    game_over(word, won, attempts)


"""
Display Hangman based on number of wrong attempts
"""


def display_hangman(attempts):
    if attempts == 0:
        hangman_result = """
        -----------
        |         |       wrong
        |         |      answers:
        |                 0 / 6
        |
        |
        |
        |
"""
    elif attempts == 1:
        hangman_result = """
        -----------
        |         |       wrong
        |         |      answers:
        |        ( )      1 / 6
        |
        |
        |
        |
"""

    elif attempts == 2:
        hangman_result = """
        -----------
        |         |       wrong
        |         |      answers:
        |        ( )      2 / 6
        |         |
        |         |
        |
        |
"""

    elif attempts == 3:
        hangman_result = r"""
        -----------
        |         |       wrong
        |        ( )     answers:
        |        \|       3 / 6
        |         |
        |
        |
        |
"""

    elif attempts == 4:
        hangman_result = r"""
        -----------
        |         |       wrong
        |         |      answers:
        |        ( )      4 / 6
        |        \|/
        |         |
        |
        |
"""

    elif attempts == 5:
        hangman_result = r"""
        -----------
        |         |       wrong
        |         |      answers:
        |        ( )      5 / 6
        |        \|/
        |         |
        |        /
        |
"""

    else:
        hangman_result = r"""
        -----------
        |         |       wrong
        |         |      answers:
        |        ( )      6 / 6
        |        \|/
        |         |        YOU
        |        / \      LOST!
        |
"""
    return hangman_result


"""
Display win or lost to player
"""


def game_over(word, won, attempts):
    if attempts >= 6:
        os.system('clear')
        print("\nSorry, " + name + ". You lost.")
        prCyan("GAME OVER.")
        prCyan("The word was " + word + ".")
        prRed(" Hangman ".center(40, "*"))
        prRed(display_hangman(attempts))
        prRed("*" * 40)
        continue_or_quit()
    if won:
        os.system('clear')
        print("\nWell done, " + name + "!\n")
        prCyan("The word was " + word + ".")
        prCyan("Congratulations, you guessed the word!\n")
        prPurple(" Hangman ".center(40, "*"))
        prPurple("*" * 40)
        prPurple("         ***         ".center(40, "*"))
        prPurple("   CONGRATULATIONS   ".center(40, "*"))
        prPurple("      YOU WON!!      ".center(40, "*"))
        prPurple("         ***         ".center(40, "*"))
        prPurple("*" * 40)
        prPurple("*" * 40)
        continue_or_quit()


"""
Ask player to continue playing or quit
"""


def continue_or_quit():
    play_again = False
    while not play_again:
        print("Would you like to play again?")
        reply = input("Enter Y to play again and N to quit.").upper()
        if reply == "Y":
            os.system('clear')
            continue_message()
        elif reply == "N":
            prCyan("\nThanks for playing today, " + name + ".\nGoodbye!\n")
            exit()
        else:
            prYellow("\nYour entry was invalid. Enter Y or N. \n")


# name is global variable, intro_message
# starts the game for the new player


name = get_name()
intro_message()
