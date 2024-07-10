import random
from wordlist import word_list

print("**************************************")
print("                                  ****")
print("WOULD YOU LIKE TO PLAY HANGMAN?   ****")
print("                                  ****")
print("**************************************\n")
name = input("Please enter your name?  ")
print("\nHello " + name + ", let's get started.\n")
print("If you make six wrong guesses, you lose!\n")

# Choose a random word from the word list
word = random.choice(word_list).upper()
print("The hangman word is: " + word)

# Convert word into a string of its letters
word_letters = list(word)
print(word_letters)

# Create list of correct letters in word with no duplicates in order to compare to guessed letters list
correct_letters = list(dict.fromkeys(word_letters))
print(correct_letters)

# Calculate number of letters in word
num_of_letters = len(word)
print("\nThe word you're trying to guess has " + str(num_of_letters) + " letters.\n")

#Create a list for positions of letters that match word
positions = [x for x in range(num_of_letters)]
# print(positions)

# Create blank spaces for each letter in word to show player in console
word_string = ["_" for x in range(num_of_letters)]
# print(word_string)
display_wordstring = " ".join(word_string)
print(display_wordstring)
print("\n")

# Create a list from word string to update as player makes correct guesses

# Create list of letters that were guessed
guessed_letters = []

# Create list of words that were guessed
guessed_words = []

# Create list of correct letters that were guessed
guessed_correct_letters = []

# Create variable to count the number of attempts
attempts = 0

# Create variable for puzzle not solved
won = False

while not won and attempts < 6:
    # Create variable for player's guess
    guess = input("\nPlease guess a letter or you can try to guess the word.  ").upper()
    if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("\nYou already guessed this letter.")
            elif guess not in word:
                print("\nThe letter guess is not correct")
                guessed_letters.append(guess)
                attempts += 1
            else:
                print("\nYour letter guess is correct.")
                guessed_letters.append(guess)
                guessed_correct_letters.append(guess)
                for position, letter in zip(positions, word_letters):
                    if word_letters[position] == guess:
                        word_string[position] = guess
                        display_wordstring = " ".join(word_string)
                print(display_wordstring)
                # Test if word is complete
                guessed_correct_letters.sort()
                correct_letters.sort()
                if guessed_correct_letters == correct_letters:
                    print("Congratulations, you won!")
                    exit()
    elif guess.isalpha() and len(guess) == len(word):
        if guess in guessed_words:
            print("You already guessed this word.")
        elif guess == word.upper():
            print("Congrats! Your word guess is correct!")
            won = True
        else:
            print("Your word guess is incorrect, please try again.")
            guessed_words.append(guess)
            attempts += 1
    else:
        print("You did not enter a letter or word, please try again.")


