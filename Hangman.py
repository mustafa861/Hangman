import random
import string
from words import words  
def get_valid_word():
    word = random.choice(words).upper()  
    while "-" in word or " " in word: 
        word = random.choice(words).upper()
    return word
def hangman():
    word = get_valid_word() 
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase) 
    used_letters = set() 
    lives = 6  
    while len(word_letters) > 0 and lives > 0:          
        print("\nYou have", lives, "lives left. Used letters:", " ".join(used_letters))
        word_display = [letter if letter in used_letters else "-" for letter in word]
        print("Current word:", " ".join(word_display))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Wrong guess!")

        elif user_letter in used_letters:
            print("You already guessed that letter. Try again.")

        else:
            print("Invalid character. Please enter a letter.")

    if lives == 0:
        print("\nYou lost! The word was:", word)
    else:
        print("\nCongratulations! You guessed the word:", word)
hangman()
