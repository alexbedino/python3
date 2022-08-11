import random
from wordshangman import words
import string

def get_valid_word(words):
    word = random.choice(words) # selecting one element in our words list we have imported above
    while "-" in word or " " in word:
        word = random.choice(words) # this ensures only actual words are selected 
    
    return word.upper() # upppercasing all letters

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #keeps track of the letters in the correct word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    lives = 6

    while len(word_letters) > 0: #when all letters are removed the while loop stops
        # letters used
        print ('You have used these letters:'," ".join(used_letters))

        # what current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters: # if it is a valid character (checking in alphabet) we haven't used yet:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 
                
        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")

        else:
            print("Invalid character. Try again")
hangman()
