import random
import string
import art

MAX_TURNS = 5

def main():
    """Chooses word and makes game repeatable"""
    choice = "1"

    while choice in ["1", "2", "3"]:
        choice = show_main_menu()
        if choice == "1":
            play_wordle()
        elif choice == "2":
            add_word_to_wordlist()
        elif choice == "3":
            remove_word_from_list()
        else:
            choice = "Stop"

def show_main_menu() -> str:
    print(art.logo)
    print("Welcome to Wordle")
    print("1. Play Wordle")
    print("2. Add word to wordlist")
    print("3. Remove word from wordlist")
    print("Pres any other button to quit")
    choice = input("(1 / 2 / 3): ")
    return choice

def get_starting_word() -> str:
    """ Gets a random word from the word list """

    with open ("wordlist.txt", "r") as word_list:
        words = word_list.read().splitlines()
        word_index = random.randint(0, len(words)-1)
        ret_word = words[word_index]

    return ret_word.lower()

def play_wordle() -> str:
    """ Main game loop """

    play = True
    while play:
        print(art.logo)
        answer = get_starting_word()

        for i in range(1, MAX_TURNS+1):
            guess = get_guess(i)
            if process_guess(guess, answer):
                print()
            else:
                break
        
        if guess.lower() != answer:
            print(art.lost)
            print(f"You lost. The Answer was: {answer}")

        print("Play Again? (Y / N)")
        repeat = input()
        if repeat.lower() != "y":
            play = False

def get_guess(current_turn) -> str:
    """Gets a guess from the player and checks it"""

    guess = ""
    
    while guess == "":
        print(f"{current_turn} / {MAX_TURNS}")
        print("Enter Guess:")
        unsafe_guess = input()

        if len(unsafe_guess.strip().strip(string.punctuation)) == 5 and not unsafe_guess.isnumeric():
            guess = unsafe_guess.lower()
        elif unsafe_guess.isnumeric():
            print("Guess cannot be a number. Try again.\n")
        else:
            print("Guess has to be 5 letters long. Try again.\n")
    
    return guess

def process_guess(guess, answer):
    """Analyzes the guess from the player and shows status"""

    if guess.lower() == answer:
        print(art.celebration)
        print(f"The answer is {answer}")
        return False

    else:
        show_string = ["-"]*5

        for i in range(5):
            if guess[i] == answer[i]:
                show_string[i] = "C"
            elif guess[i] in answer:
                show_string[i] = "c"

        print("".join(show_string))
        return True

def add_word_to_wordlist():
    pass

def remove_word_from_list():
    pass

if __name__ == "__main__":
    main()