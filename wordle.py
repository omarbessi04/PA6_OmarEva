import random
import string
from Round import Round
from UI_manager import UIManager

def main():
    """Starts Main Menu"""

    choice = "1"
    title = "Welcome to Wordle!"

    while choice in ["1", "2", "3", "4", "5"]:
        choice = show_main_menu(title)

        if choice == "1":
            title = "Welcome to Wordle!"
            game = play_wordle_round()
            while game:
                game = play_wordle_round()

        elif choice == "2":
            see_scoreboards()
        
        elif choice == "3":
            see_profiles()

        elif choice == "4":
            title = add_or_remove_word("add")

        elif choice == "5":
            title = add_or_remove_word("remove")

        else:
            choice = "Stop"

def show_main_menu(title) -> str:
    """Shows the main menu with a title"""

    ui = UIManager()
    return ui.show_main_menu(title)

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
    ui = UIManager()
    mode = ui.game_mode()

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
        ret_word = random.choice(words)

    return ret_word.lower()

def see_scoreboards():
    """Show high scores"""

    # UI
    ui = UIManager()
    choice = ui.see_scoreboards()

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

        scoreboard = sorted(scoreboard, key=lambda user: int(user.split(":")[1]), reverse=True)
        number_of_lines = len(scoreboard)
        ui.see_specified_scoreboard(scoreboard, title, number_of_lines)

def see_profiles():
    ui = UIManager()
    ui.see_profiles()

def add_or_remove_word(operation):
    """Shared text between the adding and removing functions"""

    # Show UI
    ui = UIManager()
    ui.add_remove_word(operation)
    
    # Get word length and error check
    word_length = 0
    while word_length not in ["4", "5", "7"]:
        unsafe_word_length = input()

        if unsafe_word_length not in ["4", "5", "7"]:
            print("Word length must be '4', '5', or '7' (number). Try Again")
        else:
            word_length = unsafe_word_length

    # Set word length and get filename
    word_length = int(unsafe_word_length)
    file_name = f"Wordlists/{word_length}_letter_words.txt"

    if operation == "add":
        return add_word_to_wordlist(word_length, file_name)
    else:
        return remove_word_from_list(file_name)

def add_word_to_wordlist(word_length, file_name):
    """Add word to the specified wordlist"""

    # We're going to append and read the file, so open it in r+ mode
    with open (file_name, "r+") as word_list:
        words = word_list.read().splitlines()

        # Get new word and error check
        new_word = ""
        while new_word == "":
            print("Enter new word:")
            unsafe_new_word = input()
            unsafe_new_word = unsafe_new_word.strip().strip(string.punctuation)

            if len(unsafe_new_word) != word_length:
                print(f"Word must be {word_length} letters long\n")

            elif any([letter.isnumeric() for letter in unsafe_new_word]):
                print("Letter cannot include letters\n")

            elif " " in unsafe_new_word:
                print("Word cannot include spaces\n")

            # The last thing we check on to hopefully save some time
            elif unsafe_new_word in words:
                print("Word already in wordlist\n")

            else:
                new_word = unsafe_new_word
        
        word_list.write(new_word.lower() + "\n")
    
    return f"{new_word} added to wordlist!"

def remove_word_from_list(file_name):
    """Remove word from the specified wordlist"""

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

if __name__ == "__main__":
    main()