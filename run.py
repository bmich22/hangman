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

# Calculate number of letters in word
num_of_letters = len(word)
print("\nThe word you're trying to guess has " + str(num_of_letters) + " letters.")

#Create a list for positions of letters that match word
positions = [x for x in range(num_of_letters)]

# Create blank spaces for each letter in word
word_string = "_ " * num_of_letters
print("\n" + word_string + "\n")

# Create list of letters that were guessed
guessed_letters = []

# Create list of words that were guessed
guessed_words = []

# Create variable to count the number of attempts
attempts = 0

# Create variable for puzzle not solved
won = False

# while not won and attempts < 6:
    # Create variable for player's guess
guess = input("Please guess a letter or you can try to guess the word.").upper()

# for letter in word_letters:
#     if guess == letter.upper():
#         print(letter)
#         guessed_letters.append(guess)
#         print(guessed_letters)
#         correct_letter = guess
#         print("correct")
#     else:
#         correct_letter = "wrong"
# print(correct_letter)

for position, letter in zip(positions, word_letters):
    if guess == letter.upper():
        print(position, letter)
        print("correct")
    else:
        print("not correct")


