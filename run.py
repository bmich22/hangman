import random
import os
from wordlist import word_list

# Add colors 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))

"""
Get the name of the new player 
"""
def get_name():
    prYellow("""\n
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
    new_name = input("Please enter your name:  ").capitalize()
    return new_name

""" 
Message to new player  
"""
def intro_message():
    os.system('clear')
    prCyan("\nHello, " + name + ".")
    prCyan("Guess the letters or the whole word.")
    prCyan("If you make six wrong guesses, you lose!\n")
    choose_word()

"""
Choose a random word from the word list  
"""
def choose_word():
    print("What level of difficulty would you like to play?")
    print("""
********  HANGMAN  **********
      -----------      
      |         |      
      |         |      
      |                
      |   1 = EASY             
      |   2 = INTERMEDIATE            
      |   3 = DIFFICULT            
      |                              

*****************************"""
)
    valid_choice = False
    while not valid_choice:
        difficulty = input("Please enter 1, 2 or 3 to choose a level of difficulty.")
        print(difficulty)
        if not difficulty.isnumeric():
            prYellow("Invalid. Your entry was not a number. ")
        difficulty = int(difficulty)
        if difficulty ==0:
            prYellow("Invalid. Your entry was not a 1, 2 or 3. ")
    word = random.choice(word_list[difficulty]).upper()
    print(word)   
    os.system('clear')
    prCyan("\nOkay, "+ name.capitalize() + "\nLet's begin!")
    play_game(word)

"""
Message to continuing player 
"""
def continue_message():
    prCyan("\nHello again, " + name.capitalize() + ".")
    prCyan("Guess the letters or the whole word.")
    prCyan("If you make six wrong guesses, you lose!\n")
    choose_word()
    play_game(word)

# # Add colors
# def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
 
# def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
 
# def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
 
# def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
 
# def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
 
"""
Play game  
"""
def play_game(word):
    # Convert word into a list of its letters
    word_letters = list(word)

    # Create list of correct letters in word with no 
    # duplicates in order to compare to guessed letters list
    correct_letters = list(dict.fromkeys(word_letters))

    # Calculate number of letters in word
    num_of_letters = len(word)

    #Create a list for number positions of letters that match word
    positions = [x for x in range(num_of_letters)]

    # Create a string of dashes for each letter in word 
    word_string = ["_" for x in range(num_of_letters)]
    display_wordstring = " ".join(word_string)

    # Create variables for guesses
    guessed_letters = []
    guessed_words = []
    guessed_correct_letters = []

    # Create variable to count the number of wrong attempts
    attempts = 0

    # Create variable for puzzle not solved
    won = False

    message = ""

    while not won and attempts < 6:
        # Create variable for player's guess and
        # print messages and outcomes
        print(display_hangman(attempts))
        prCyan("The word you're trying to guess has " + str(num_of_letters) + " letters.\n")
        print("Letters already chosen: ")
        print(guessed_letters)
        print("\n")
        prCyan(display_wordstring)
        prYellow(message)
        guess = input("Please guess a letter or you can try to guess the word.\n").upper()
        if guess.isalpha() and len(guess) == 1:
                if guess in guessed_letters:
                    os.system('clear')
                    message = "\nYou already guessed the letter " + guess + "."
                elif guess not in word:
                    os.system('clear')
                    message = "\nIncorrect! There is no letter " + guess + " in the word."
                    guessed_letters.append(guess)
                    attempts += 1
                else:
                    os.system('clear')
                    message ="\nCorrect! " + guess + " is in the word."
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
                        won=True
        elif guess.isalpha() and len(guess) > 1:
            if guess in guessed_words:
                message = "/nYou already guessed this word."
            elif guess == word.upper():
                message = "Congrats! Your word guess is correct!"
                won = True
            else:
                os.system('clear')
                message = "Your word guess is incorrect, please try again."
                guessed_words.append(guess)
                attempts += 1
        else:
            os.system('clear')
            message = "Oops!!\nYou did not enter a letter or word, please try again.\n"
    game_over(word, won, attempts)

"""
Display Hangman based on number of wrong attempts
"""  
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

"""
Show win or lost to player  
"""
def game_over(word, won, attempts):
    if attempts >= 6:
        os.system('clear')
        print("\n ")
        prCyan("GAME OVER!\n")
        prCyan("Sorry, " + name + ". You lost.\n The word was " + word + ".")    
        prRed(display_hangman(attempts))
        continue_or_quit()
    if won:
        os.system('clear')
        print("\n ")
        prCyan("WELL DONE, " + name + "!\n")
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

"""
Ask player to continue playing or quit 
""" 
def continue_or_quit():
    play_again = False
    while not play_again:
        reply = input("\nWould you like to play again?\nPlease enter Y to play again and N to quit.").upper()
        if reply == "Y":
            os.system('clear')
            continue_message()
        elif reply == "N":
            prCyan("\nThank you for playing today.\nGoodbye!\n")
            exit()
        else:
            print("\nYour entry was invalid.\n")

# Name is global variable, intro_message 
# starts the game for the new player
name = get_name()
intro_message()

    


    

