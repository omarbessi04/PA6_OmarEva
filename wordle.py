import random
import art
import string
import os
from Round import Round

def main():
    """Starts Main Menu"""

    choice = "1"
    title = "Welcome to Wordle!"
    while choice in ["1", "2", "3"]:
        choice = show_main_menu(title)

        if choice == "1":
            title = "Welcome to Wordle!"
            game = play_wordle_round()
            while game:
                game = play_wordle_round()

        elif choice == "2":
            title = add_word_to_wordlist()

        elif choice == "3":
            title = remove_word_from_list()

        else:
            choice = "Stop"

def show_main_menu(title) -> str:
    """Shows the main menu with an optional title"""

    os.system('cls' if os.name == 'nt' else 'clear')
    print(art.logo)
    print(title)
    print("1. Play Wordle")
    print("2. Add word to wordlist")
    print("3. Remove word from wordlist")
    print("Pres any other button to quit")
    choice = input("(1 / 2 / 3): ")
    return choice

def play_wordle_round() -> bool:
    """Plays a repeatable round of Wordle"""

    settings = game_mode()
    word = get_starting_word(settings["Wordlength"])

    new_round = Round(word, settings["Wordlength"], settings["Max Guesses"])
    os.system('cls' if os.name == 'nt' else 'clear')
    new_round.play_round()

    print("Play Again? (Y / N)")
    repeat = input()
    if repeat.lower() == "y":
        return True

def game_mode():
    """Edits the settigns of the game"""

    settings ={"Wordlength": 5, "Max Guesses": 5}

    os.system('cls' if os.name == 'nt' else 'clear')
    print(art.game_mode)
    print("Pick Game Mode:")
    print("1. Normal\n\t5 letter word, 5 guesses\n")
    print("2. Squadrant\n\t4 letter word, 6 guesses\n")
    print("3. Rule of 7\n\t7 letter word, 7 guesses\n")
    print("\nIgnore to play Normal mode")
    mode = input("(1 / 2 / 3):\n")

    if mode == "2":
        settings ={"Wordlength": 4, "Max Guesses": 6}

    if mode == "3":
        settings ={"Wordlength": 7, "Max Guesses": 7}

    return settings

def get_starting_word(wordlength) -> str:
    """ Gets a random word from the word list """

    file_name = f"Wordlists/{wordlength}_letter_words.txt"
    with open (file_name, "r") as word_list:
        words = word_list.read().splitlines()
        ret_word = ""
        # All word files have a new line at the end of them
        # so we don't want to pick the last word, so -2
        word_index = random.randint(0, len(words)-2)
        ret_word = words[word_index]

    return ret_word.lower()

def add_word_to_wordlist():
    """Add word to the specified wordlist"""

    # Show UI
    os.system('cls' if os.name == 'nt' else 'clear')
    print(art.settings)
    print("First enter the length of the word to be added")
    print("(Must be 4, 5, or 7)")

    # Get word length and error check
    word_length = 0
    while word_length not in ["4", "5", "7"]:
        unsafe_word_length = input()
        if unsafe_word_length not in ["4", "5", "7"]:
            print("Word length must be 4, 5, or 7. Try Again")
        else:
            word_length = unsafe_word_length

    # Set word length and get filename
    word_length = int(unsafe_word_length)
    file_name = f"Wordlists/{word_length}_letter_words.txt"


    with open (file_name, "r+") as word_list:
        words = word_list.read().splitlines()

        # Get new word and error check
        new_word = ""
        while new_word == "":
            print("Enter new word:")
            unsafe_new_word = input().strip().strip(string.punctuation)

            if len(unsafe_new_word) != word_length:
                print(f"Word must be {word_length} letters long")

            elif any([letter.isnumeric() for letter in unsafe_new_word]):
                print("Letter cannot include letters")

            # The last thing we check on to hopefully save some time
            elif unsafe_new_word in words:
                print("Word already in wordlist")

            else:
                new_word = unsafe_new_word
        
        word_list.write(new_word.lower() + "\n")
    
    return f"{new_word} added to wordlist!"

def remove_word_from_list():
    """Remove word from the specified wordlist"""

    # Show UI
    os.system('cls' if os.name == 'nt' else 'clear')
    print(art.settings)
    print("First enter the length of the word that you want to remove")
    print("(Must be 4, 5, or 7)")

    # Get word length and error check
    word_length = 0
    while word_length not in ["4", "5", "7"]:
        unsafe_word_length = input()
        if unsafe_word_length not in ["4", "5", "7"]:
            print("Word length must be 4, 5, or 7. Try Again")
        else:
            word_length = unsafe_word_length

    # Set word length and get filename
    word_length = int(unsafe_word_length)
    file_name = f"Wordlists/{word_length}_letter_words.txt"


    with open (file_name, "r") as word_list_file:
        old_word_list = word_list_file.read().splitlines()

    # Get new word and error check
    word_amount = len(old_word_list)

    while len(old_word_list) == word_amount:
        print("Enter the word you want to remove:")
        bad_word = input().lower()

        if bad_word in old_word_list:
            old_word_list.remove(bad_word)
            
        else:
            print(f"{bad_word} not in wordlist. Try Again (Y / N)?")
            repeat = input()
            if repeat.lower() != "y":
                break

    with open (file_name, "w") as new_word_list:
        for word in old_word_list:
            new_word_list.write(word + "\n")

    return f"{bad_word} removed from wordlist"

if __name__ == "__main__":
    main()