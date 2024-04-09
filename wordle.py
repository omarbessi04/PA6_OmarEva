import random
import art
import string
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
    new_round.play_round()

    print("Play Again? (Y / N)")
    repeat = input()
    if repeat.lower() == "y":
        return True

def game_mode():
    """Edits the settigns of the game"""

    settings ={"Wordlength": 5, "Max Guesses": 5}

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
        word_index = random.randint(0, len(words)-1)
        ret_word = words[word_index]

    return ret_word.lower()

def add_word_to_wordlist():
    print(art.settings)
    print("First enter the length of the word to be added")
    print("(Must be 4, 5, or 7)")

    word_length = 0
    while word_length not in ["4", "5", "7"]:
        unsafe_word_length = input()
        if unsafe_word_length not in ["4", "5", "7"]:
            print("Word length must be 4, 5, or 7. Try Again")
        else:
            word_length = unsafe_word_length

    word_length = int(unsafe_word_length)
    file_name = f"Wordlists/{word_length}_letter_words.txt"

    with open (file_name, "r+") as word_list:
        words = word_list.read().splitlines()

        new_word = ""
        while new_word == "":
            print("Enter new word:")
            unsafe_new_word = input().strip().strip(string.punctuation)
            if len(unsafe_new_word) != word_length:
                print(f"Word must be {word_length} letters long")
            elif unsafe_new_word in words:
                print("Word already in wordlist")
            elif any([letter.isnumeric() for letter in unsafe_new_word]):
                print("Letter cannot include letters")
            else:
                new_word = unsafe_new_word
        
        word_list.write("\n"+new_word)
    
    return f"{new_word} added to wordlist!"

def remove_word_from_list():
    pass

if __name__ == "__main__":
    main()