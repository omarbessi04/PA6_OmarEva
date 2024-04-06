import random
import string
import art

MAX_TURNS = 5

def main():
    """Creates word and makes game repeatable"""

    play = True
    while play:
        
        answer = get_starting_word()
        repeat = play_wordle(answer)
        
        if repeat.lower() != "y":
            play = False

def get_starting_word() -> str:
    """ Gets a random word from the word list """

    with open ("wordlist.txt", "r") as word_list:
        words = word_list.read().splitlines()
        word_index = random.randint(0, len(words)-1)
        ret_word = words[word_index]

    return ret_word.lower()

def play_wordle(answer):
    """ Main game loop """

    print(art.logo)
    for i in range(1, MAX_TURNS+1):
        guess = get_guess(i)
        process_guess(guess, answer)
        print()
    
    if guess.lower() != answer:
        print(art.lost)
        print(f"You lost. The Answer was: {answer}")

    print("Play Again? (Y / N)")
    repeat = input()
    return repeat

def get_guess(current_turn) -> str:
    """Gets a guess from the player and checks it"""

    guess = ""
    
    while guess == "":
        print(f"{current_turn} / {MAX_TURNS}")
        print("Enter Guess:")
        unsafe_guess = input()

        if len(unsafe_guess.strip().strip(string.punctuation)) == 5:
            guess = unsafe_guess
        else:
            print("Guess has to be 5 letters long. Try again.\n")
    
    return guess

def process_guess(guess, answer):
    """Analyzes the guess from the player and shows status"""

    if guess.lower() == answer:
        print(art.celebration)
        print(f"The answer is {answer}")

    else:
        show_string = ["-"]*5

        for i in range(5):
            if guess[i] == answer[i]:
                show_string[i] = "C"
            elif guess[i] in answer:
                show_string[i] = "c"

    print("".join(show_string))

if __name__ == "__main__":
    main()