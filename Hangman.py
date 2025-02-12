import random
import string
from words import words  # Ensure 'words' is a list of words

def get_valid_word():
    word = random.choice(words).upper()  # Convert to uppercase for consistency
    while "-" in word or " " in word:  # Ensure no hyphen or space in the word
        word = random.choice(words).upper()
    return word

def hangman():
    word = get_valid_word()  # Get a valid word
    word_letters = set(word)  # Set of unique letters in the word
    alphabet = set(string.ascii_uppercase)  # All uppercase letters
    used_letters = set()  # Tracks guessed letters
    lives = 6  # Number of incorrect guesses allowed

    while len(word_letters) > 0 and lives > 0:
        # Show used letters
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

# Run the game
hangman()
