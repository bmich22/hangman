import random
from wordlist import word_list

print("**************************************")
print("LET'S PLAY HANGMAN!   ****************")
print("**************************************")
name = input("What is your name?  ")
print("\nHello " + name + ", let's get started.\n")

word = random.choice(word_list)
print("The hangman word is: " + word)