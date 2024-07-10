import random
import os
from wordlist import word_list

print("**************************************")
print("                                  ****")
print("WOULD YOU LIKE TO PLAY HANGMAN?   ****")
print("                                  ****")
print("**************************************\n")
name = input("Please enter your name?  ")
os.system('clear')
print("\nHello, " + name.capitalize() + ".\n")
print("If you make six wrong guesses, you lose!\n")
print("Let's begin.")

# Choose a random word from the word list
word = random.choice(word_list).upper()

# Convert word into a string of its letters
word_letters = list(word)

# Create list of correct letters in word with no duplicates in order to compare to guessed letters list
correct_letters = list(dict.fromkeys(word_letters))

# Calculate number of letters in word
num_of_letters = len(word)

#Create a list for positions of letters that match word
positions = [x for x in range(num_of_letters)]

# Create blank spaces for each letter in word to show player in console
word_string = ["_" for x in range(num_of_letters)]
display_wordstring = " ".join(word_string)

# Create list of letters that were guessed
guessed_letters = []

# Create list of words that were guessed
guessed_words = []

# Create list of correct letters that were guessed
guessed_correct_letters = []

# Create variable to count the number of wrong attempts
attempts = 0

# Create variable for puzzle not solved
won = False

def game_over(won, attempts):
    if attempts >= 6:
        os.system('clear')
        print("\n")
        print("GAME OVER!\nYou lost.\nThe word was " + word + ".")    
        print(display_hangman(attempts))
        # add function to play again or quit
    if won:
        print("The word was " + word +".")
        print("""
        ********  HANGMAN  **********
        *****************************
        ***                       ***
        ***    CONGRATULATIONS    ***
        ***       YOU WON!!       ***
        ***                       ***
        ***                       ***
        *****************************
        *****************************
        """)
        # add function to play again or quit

def display_hangman(attempts):
    if attempts == 0:
        hangman_result = """
        ********  HANGMAN  **********
        *****************************
        ***      -----------      ***
        ***      |         |      ***
        ***      |         |      ***
        ***      |                ***
        ***      |                ***
        ***      |                ***
        ***      |                ***
        ***      |                ***
        ***      |                ***
        ***                       ***
        *** YOU HAVE SIX CHANCES  ***
        *****************************
        """
    elif attempts == 1:
        hangman_result = """
        *****************************
        ***      -----------      ***
        ***      |         |      ***
        ***      |         |      ***
        ***      |        ( )     ***
        ***      |                ***
        ***      |                ***
        ***      |                ***
        ***      |                ***
        ***      |                ***
        ***                       ***
        *** YOU HAVE FIVE CHANCES ***
        *****************************
        """

    elif attempts == 2:
        hangman_result = """
        *****************************
        ***      -----------      ***
        ***      |         |      ***
        ***      |         |      ***
        ***      |        ( )     ***
        ***      |         |      ***
        ***      |         |      ***
        ***      |                ***
        ***      |                ***
        ***                       ***
        *** YOU HAVE FOUR CHANCES ***
        *****************************
        """

    elif attempts == 3:
        hangman_result = """
        *****************************
        ***      -----------      ***
        ***      |         |      ***
        ***      |         |      ***
        ***      |        ( )     ***
        ***      |        \|      ***
        ***      |         |      ***
        ***      |                ***
        ***      |                ***
        ***                       ***
        *** YOU HAVE THREE CHANCES **
        *****************************
        """

    elif attempts == 4:
        hangman_result = """
        *****************************
        ***      -----------      ***
        ***      |         |      ***
        ***      |         |      ***
        ***      |        ( )     ***
        ***      |        \|/     ***
        ***      |         |      ***
        ***      |                ***
        ***      |                ***
        ***                       ***
        ***  YOU HAVE TWO CHANCES ***
        *****************************
        """
         

    elif attempts == 5:
        hangman_result = """
        *****************************
        ***      -----------      ***
        ***      |         |      ***
        ***      |         |      ***
        ***      |        ( )     ***
        ***      |        \|/     ***
        ***      |         |      ***
        ***      |        /       ***
        ***      |                ***
        ***                       ***
        ** YOU HAVE ONE MORE CHANCE *
        *****************************
        """

    else:
        hangman_result = """
        *****************************
        ***      -----------      ***
        ***      |         |      ***
        ***      |         |      ***
        ***      |        ( )     ***
        ***      |        \|/     ***
        ***      |         |      ***
        ***      |        / \     ***
        ***      |                ***
        ***                       ***
        ***   SORRY, YOU LOST!    ***
        *****************************
        """
    return hangman_result

while not won and attempts < 6:
    # Create variable for player's guess
    print(display_hangman(attempts))
    print("The word you're trying to guess has " + str(num_of_letters) + " letters.\n")
    print(display_wordstring)
    print("\n")
    guess = input("Please guess a letter or you can try to guess the word.  ").upper()
    if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                os.system('clear')
                print("\nYou already guessed the letter " + guess + ".")
                print("\n")
            elif guess not in word:
                os.system('clear')
                print("\nIncorrect! There is no letter " + guess + " in the word.")
                guessed_letters.append(guess)
                attempts += 1
            else:
                os.system('clear')
                print("\nCorrect! " + guess + " is in the word.")
                guessed_letters.append(guess)
                guessed_correct_letters.append(guess)
                for position, letter in zip(positions, word_letters):
                    if word_letters[position] == guess:
                        word_string[position] = guess
                        display_wordstring = " ".join(word_string)
                # Test if word is complete
                guessed_correct_letters.sort()
                correct_letters.sort()
                print(guessed_correct_letters)
                print(correct_letters)
                if guessed_correct_letters == correct_letters:
                    won=True
    elif guess.isalpha() and len(guess) > 1:
        if guess in guessed_words:
            print("You already guessed this word.")
        elif guess == word.upper():
            print("Congrats! Your word guess is correct!")
            won = True
        else:
            os.system('clear')
            print("Your word guess is incorrect, please try again.")
            guessed_words.append(guess)
            attempts += 1
    else:
        os.system('clear')
        print("You did not enter a letter or word, please try again.")
game_over(won, attempts)
