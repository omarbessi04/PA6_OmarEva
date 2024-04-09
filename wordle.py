import random
import art
import string
import os
import math
from Round import Round

def main():
    """Starts Main Menu"""

    choice = "1"
    title = "Welcome to Wordle!"
    while choice in ["1", "2", "3", "4"]:
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

        elif choice == "4":
            see_high_scores()

        else:
            choice = "Stop"

def show_main_menu(title) -> str:
    """Shows the main menu with a title"""

    os.system('cls' if os.name == 'nt' else 'clear')
    print(art.logo)
    print(title)
    print("1. Play Wordle")
    print("2. Add word to wordlist")
    print("3. Remove word from wordlist")
    print("4. See high scores")
    print("Press any other button to quit")
    choice = input("(1 / 2 / 3 / 4): ")
    return choice

def play_wordle_round() -> bool:
    """Plays a repeatable round of Wordle"""

    game_mode = choose_game_mode()
    word = get_starting_word(game_mode["Wordlength"])

    new_round = Round(word, game_mode["Wordlength"], game_mode["Max Guesses"])
    os.system('cls' if os.name == 'nt' else 'clear')
    new_round.play_round()

    print("Play Again? (Y / N)")
    repeat = input()
    if repeat.lower() == "y":
        return True

def choose_game_mode():
    """Choose a game mode"""

    # UI
    os.system('cls' if os.name == 'nt' else 'clear')
    print(art.game_mode)
    print("Pick Game Mode:")
    print("1. Normal\n\t5 letter word, 5 guesses\n")
    print("2. Squadrant\n\t4 letter word, 6 guesses\n")
    print("3. Rule of 7\n\t7 letter word, 7 guesses\n")
    print("\nIgnore to play Normal mode")
    mode = input("(1 / 2 / 3):\n")

    # Change setting according to user choice
    if mode == "2":
        settings ={"Wordlength": 4, "Max Guesses": 6}

    elif mode == "3":
        settings ={"Wordlength": 7, "Max Guesses": 7}

    else:
        settings ={"Wordlength": 5, "Max Guesses": 5}

    return settings

def get_starting_word(wordlength) -> str:
    """ Gets a random word from the word list """

    # file names differ only by a single number, the wordlength
    file_name = f"Wordlists/{wordlength}_letter_words.txt"

    with open (file_name, "r") as word_list:
        words = word_list.read().splitlines()
        ret_word = ""
        # All word files have a new line at the end of them
        # so we don't want to pick the last word, so we use a -2 here
        word_index = random.randint(0, len(words)-2)
        ret_word = words[word_index]

    return ret_word.lower()

def add_word_to_wordlist():
    """Add word to the specified wordlist"""


    word_length, file_name = show_adding_removing_UI("add")

    # We're going to append and read the file, so open it in r+ mode
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

            elif " " in unsafe_new_word:
                print("Word cannot include spaces")

            # The last thing we check on to hopefully save some time
            elif unsafe_new_word in words:
                print("Word already in wordlist")

            else:
                new_word = unsafe_new_word
        
        word_list.write(new_word.lower() + "\n")
    
    return f"{new_word} added to wordlist!"

def remove_word_from_list():
    """Remove word from the specified wordlist"""

    word_length, file_name = show_adding_removing_UI("remove")

    with open (file_name, "r") as word_list_file:
        old_word_list = word_list_file.read().splitlines()

    # Get new word and error check
    word_amount = len(old_word_list)
    while len(old_word_list) == word_amount:
        print("Enter the word you want to remove:")
        bad_word = input().lower()

        # If the word is in the list, remove it
        if bad_word in old_word_list:
            old_word_list.remove(bad_word)
            response = f"{bad_word} removed from wordlist"
            
        # The user might have expected the word to be there,
        # so give them a chance to exit here
        else:
            print(f"{bad_word} not in wordlist. Try Again (Y / N)?")
            repeat = input()
            if repeat.lower() != "y":
                response = "Word removal cancelled"
                break

    # Rewrite word file
    with open (file_name, "w") as new_word_list:
        for word in old_word_list:
            new_word_list.write(word + "\n")

    return response

def show_adding_removing_UI(word):
    """Shared text between the adding and removing functions"""

    # Show UI
    os.system('cls' if os.name == 'nt' else 'clear')
    print(art.settings)
    print(f"First enter the length of the word that you want to {word}")
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

    return word_length, file_name

def see_high_scores():
    """Show high scores"""

    # UI
    os.system('cls' if os.name == 'nt' else 'clear')
    print(art.high_scores)
    print("Choose scoreboard")
    print("1. Normal Mode")
    print("2. Rule of 7")
    print("3. Squadrant")
    print("(1 / 2 / 3):")
    choice = input()

    # Open the correct folder based on user input
    file_name, title = None, None
    if choice == "1":
        file_name = "high_scores/5wordle_scores.txt"
        title = "NORMAL MODE"

    elif choice == "2":
        file_name = "high_scores/rule_of_7_scores.txt"
        title = "RULE OF 7"

    elif choice == "3":
        file_name = "high_scores/squadrant_scores.txt"
        title = "SQUADRANT MODE"

    # Show highscores if user input is valid
    if file_name and title:

        with open(file_name) as word_data:
            scoreboard = word_data.read().splitlines()
        number_of_lines = len(scoreboard)

        # clear screen and show UI
        os.system('cls' if os.name == 'nt' else 'clear')
        print(art.high_scores)
        print(" -- " + title + " -- ")

        # Check there is any data in the file
        if number_of_lines == 0:
            print("No data available for this game mode")

        else:
            # base the number of spaces on the longest word in the file
            longest_word_length = max([len(word) for word in scoreboard])

            for i in range(number_of_lines):
                # find correct number of spaces
                number_of_spaces = (2 * longest_word_length - len(scoreboard[i])) // 2
                spaces = " " * number_of_spaces

                # Words of odd length need one more space
                if len(scoreboard[i]) % 2 == 0:
                    print("|" + spaces + scoreboard[i] + spaces + "|")
                else:
                    print("|" + spaces + scoreboard[i] + spaces + " |")

            input("\nPress enter to quit\n")

if __name__ == "__main__":
    main()