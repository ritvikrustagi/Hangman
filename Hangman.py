import random

WORDS_FILE = "words.txt"

def load_word_list():
    """Loads a list of words from a file."""
    print("Loading word list from file...")
    with open(WORDS_FILE, 'r') as file:
        words = file.readline().split()
    print(f"  {len(words)} words loaded.")
    return words

def select_word(word_list):
    """Selects and returns a random word from the list."""
    return random.choice(word_list)

word_list = load_word_list()

def is_all_letters_guessed(secret_word, guessed_letters):
    """Checks if all letters of the secret word have been guessed."""
    return all(letter in guessed_letters for letter in secret_word)

def get_partial_word(secret_word, guessed_letters):
    """Generates a string showing the correctly guessed letters and underscores for remaining ones."""
    return ''.join([letter if letter in guessed_letters else '_ ' for letter in secret_word])

def get_remaining_letters(guessed_letters):
    """Returns a string of the remaining letters that haven't been guessed yet."""
    import string
    return ''.join([letter for letter in string.ascii_lowercase if letter not in guessed_letters])

def start_game(secret_word):
    """Starts the Hangman game."""
    print("Welcome to Hangman!")
    print(f"I have chosen a word that is {len(secret_word)} letters long.")

    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 8
    
    while incorrect_guesses < max_incorrect_guesses:
        if is_all_letters_guessed(secret_word, guessed_letters):
            print("-------------")
            print("Congrats! You guessed the word!")
            break
        else:
            print("-------------")
            print(f"You have {max_incorrect_guesses - incorrect_guesses} guesses left.")
            print(f"Remaining letters: {get_remaining_letters(guessed_letters)}")
            guess = input("Guess a letter: ").lower()

            if guess in guessed_letters:
                print(f"Oops! You've already guessed that letter: {get_partial_word(secret_word, guessed_letters)}")
            elif guess in secret_word:
                guessed_letters.append(guess)
                print(f"Good guess: {get_partial_word(secret_word, guessed_letters)}")
            else:
                guessed_letters.append(guess)
                incorrect_guesses += 1
                print(f"Oops! That letter is not in the word: {get_partial_word(secret_word, guessed_letters)}")

        if incorrect_guesses == max_incorrect_guesses:
            print("-------------")
            print(f"Sorry, you ran out of guesses. The word was: {secret_word}")
            break

secret_word = select_word(word_list).lower()
start_game(secret_word)
