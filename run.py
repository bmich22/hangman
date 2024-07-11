import random
import os
from wordlist import word_list

# Add colors
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))

def get_name():
    print("""\n
LET'S PLAY A GAME OF HANGMAN.
""")
    prCyan("""
*****************************""") 
    prRed("""
      -----------      
      |         |      
      |         |      
      |                
      |                
      |                
      |                
      |                
      |    
    """)            
    
    prCyan("""                        
*****************************\n""")
    new_name = input("Please enter your name:  ")
    # prCyan("\nHello, " + new_name.capitalize() + ".\n")
    # prCyan("If you make six wrong guesses, you lose!\n")
    # prCyan("Let's begin.")
    return new_name

def intro_message():
    os.system('clear')
    prCyan("\nHello, " + name.capitalize() + ".\n")
    prCyan("Guess letters or the whole word!\n")
    prCyan("If you make six wrong guesses, you lose!\n")
    prCyan("Let's begin.")
    choose_word()

# Choose a random word from the word list
def choose_word():
    word = random.choice(word_list).upper()
    return word

def continue_message():
    prCyan("\nHello again, " + name.capitalize() + ".\n")
    prCyan("If you make six wrong guesses, you lose!\n")
    prCyan("Here we go.")
    choose_word()

# # Add colors
# def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
 
# def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
 
# def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
 
# def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
 
# def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
 
# # def get_name():
# #     print("""\n
# # LET'S PLAY A GAME OF HANGMAN.
# # """)
# #     prCyan("""
# # *****************************""") 
# #     prRed("""
# #       -----------      
# #       |         |      
# #       |         |      
# #       |                
# #       |                
# #       |                
# #       |                
# #       |                
# #       |    
# #     """)            
    
# #     prCyan("""                        
# # *****************************\n""")
# #     new_name = input("Please enter your name:  ")
# #     main(name)

# # def intro_message():
# #     prCyan("\nHello, " + name.capitalize() + ".\n")
# #     prCyan("If you make six wrong guesses, you lose!\n")
# #     prCyan("Let's begin.")

# # def continue_message():
# #     prCyan("\nHello again, " + name.capitalize() + ".\n")
# #     prCyan("If you make six wrong guesses, you lose!\n")
# #     prCyan("Here we go.")


# Play game
def play_game():
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

    while not won and attempts < 6:
        # Create variable for player's guess
        print(display_hangman(attempts))
        prCyan(name)
        prCyan("The word you're trying to guess has " + str(num_of_letters) + " letters.\n")
        prCyan(display_wordstring)
        print("\n")
        guess = input("Please guess a letter or you can try to guess the word.  ").upper()
        if guess.isalpha() and len(guess) == 1:
                if guess in guessed_letters:
                    os.system('clear')
                    prCyan("\nYou already guessed the letter " + guess + ".")
                    print("\n")
                elif guess not in word:
                    os.system('clear')
                    prCyan("\nIncorrect! There is no letter " + guess + " in the word.")
                    guessed_letters.append(guess)
                    attempts += 1
                else:
                    os.system('clear')
                    prCyan("\nCorrect! " + guess + " is in the word.")
                    guessed_letters.append(guess)
                    guessed_correct_letters.append(guess)
                    for position, letter in zip(positions, word_letters):
                        if word_letters[position] == guess:
                            word_string[position] = guess
                            display_wordstring = " ".join(word_string)
                    # Test if word is complete
                    guessed_correct_letters.sort()
                    correct_letters.sort()
                    # print(guessed_correct_letters)
                    # print(correct_letters)
                    if guessed_correct_letters == correct_letters:
                        won=True
        elif guess.isalpha() and len(guess) > 1:
            if guess in guessed_words:
                prCyan("/nYou already guessed this word.")
            elif guess == word.upper():
                prCyan("Congrats! Your word guess is correct!")
                won = True
            else:
                os.system('clear')
                prCyan("Your word guess is incorrect, please try again.")
                guessed_words.append(guess)
                attempts += 1
        else:
            os.system('clear')
            prCyan("Oops!!\nYou did not enter a letter or word, please try again.\n")
    game_over(won, attempts)

# Display Hangman based on number of wrong attempts
def display_hangman(attempts):
    if attempts == 0:
        hangman_result = """
********  HANGMAN  **********

      -----------      
      |         |      
      |         |      
      |                
      |                
      |                
      |                
      |                
      |                
                       
    WRONG ANSWERS: 0 / 6

*****************************
        """
    elif attempts == 1:
        hangman_result = """
********  HANGMAN  **********
      -----------      
      |         |      
      |         |      
      |        ( )     
      |                
      |                
      |                
      |                
      |                
                       
    WRONG ANSWERS: 1 / 6 

*****************************
        """

    elif attempts == 2:
        hangman_result = """
********  HANGMAN  **********
      -----------      
      |         |      
      |         |      
      |        ( )     
      |         |      
      |         |      
      |                
      |                
                       
    WRONG ANSWERS: 2 / 6 

*****************************"""

    elif attempts == 3:
        hangman_result = r"""
********  HANGMAN  **********
      -----------      
      |         |      
      |         |      
      |        ( )     
      |        \|      
      |         |      
      |                
      |                
                       
    WRONG ANSWERS: 3 / 6

*****************************"""

    elif attempts == 4:
        hangman_result = r"""
********  HANGMAN  **********
      -----------      
      |         |      
      |         |      
      |        ( )     
      |        \|/      
      |         |      
      |                
      |                
                       
    WRONG ANSWERS: 4 / 6 

*****************************"""
         

    elif attempts == 5:
        hangman_result = r"""
********  HANGMAN  **********
      -----------      
      |         |      
      |         |      
      |        ( )     
      |        \|/      
      |         |      
      |        /       
      |              
                       
    WRONG ANSWERS: 5 / 6

*****************************"""

    else:
        hangman_result = r"""
********  HANGMAN  **********
      -----------      
      |         |      
      |         |      
      |        ( )     
      |        \|/      
      |         |      
      |        / \      
      |              
                       
WRONG ANSWERS: 6/6  YOU LOST!

*****************************"""
    return hangman_result

# Show win or lost to player
def game_over(won, attempts):
    if attempts >= 6:
        os.system('clear')
        print("\n ")
        prCyan("GAME OVER!\n")
        prCyan("You lost.\n The word was " + word + ".")    
        prRed(display_hangman(attempts))
        continue_or_quit()
    if won:
        os.system('clear')
        print("\n ")
        prCyan("WELL DONE!\n")
        prCyan("The word was " + word +".\n")
        prCyan("Congratulations, you guessed the word!\n")
        prPurple("""
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
        continue_or_quit()

# Ask player to continue playing or quit
def continue_or_quit():
    print()
    play_again = False
    while not play_again:
        reply = input("\nWould you like to play again?\nPlease enter Y to play again and N to quit.").upper()
        if reply == "Y":
            os.system('clear')
            play_again = True
            continue_message()
        elif reply == "N":
            prCyan("\nThank you for playing today.\nGoodbye!\n")
            exit()
        else:
            print("\nYour entry was invalid.\n")

name = get_name()
intro_message()
word = choose_word()
play_game()

# # Main function    
# def main(name):
# #     print("""\n
# # LET'S PLAY A GAME OF HANGMAN.
# # """)
# #     prCyan("""
# # *****************************""") 
# #     prRed("""
# #       -----------      
# #       |         |      
# #       |         |      
# #       |                
# #       |                
# #       |                
# #       |                
# #       |                
# #       |    
# #     """)            
    
# #     prCyan("""                        
# # *****************************\n""")
# #     name = input("Please enter your name:  ")
# #     os.system('clear')
# #     prCyan("\nHello, " + name.capitalize() + ".\n")
# #     prCyan("If you make six wrong guesses, you lose!\n")
# #     prCyan("Let's begin.")
# #     # name = get_name()
#     word = choose_word()
#     play_game(word)

# if __name__ == "__main__":
#     main()

# Main function    
# def main(name):
#     word = choose_word()
#     play_game(word)

# if __name__ == "__main__":
#     main()


    

