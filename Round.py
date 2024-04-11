import string
import art
import random
from UI_manager import UIManager


class Round:
    """A round of Wordle"""

    def __init__(self, answer, wordlength, max_guesses) -> None:
        """Initialize a round of wordle"""

        self.answer = answer
        self.wordlength = wordlength
        self.max_guesses = max_guesses
        self.guesses = []
        self.score = max_guesses

    def play_round(self) -> str:
        """Main game loop"""

        print(art.logo)

        for i in range(1, self.max_guesses + 1):
            guess = self.get_guess(i)
            if self.process_guess(guess):

                ui = UIManager()
                ui.play_round()
                self.print_previous_guesses()

            else:
                break

        if guess != self.answer:
            UIManager().lose_game(self.answer)

        self.store_score()

    def get_guess(self, current_turn) -> str:
        """Gets a guess from the player and checks it"""

        guess = ""

        while guess == "":
            print(f"{current_turn} / {self.max_guesses}")
            print("Enter Guess:")
            unsafe_guess = input()

            # error check
            if (
                len(unsafe_guess.strip().strip(string.punctuation)) == self.wordlength
                and not unsafe_guess.isnumeric()
            ):
                guess = unsafe_guess.lower()

            elif unsafe_guess.isnumeric():
                print("Guess cannot be a number. Try again.\n")

            else:
                print(f"Guess has to be {self.wordlength} letters long. Try again.\n")

        return guess

    def process_guess(self, guess):
        """Analyzes the guess from the player and shows status"""

        if guess == self.answer:
            ui = UIManager()
            ui.win_game(self.answer)
            return False

        else:
            self.score -= 1
            show_string = ["-"] * self.wordlength

            for i in range(self.wordlength):
                if guess[i] == self.answer[i]:
                    show_string[i] = "C"
                elif guess[i] in self.answer:
                    show_string[i] = "c"

            self.guesses.append([guess, "".join(show_string)])

            return True

    def print_previous_guesses(self):
        ui = UIManager()
        ui.print_previous_guesses(self.guesses)

    def store_score(self):
        print()
        print("Enter nickname:")
        print("(NO NAUGHTY WORDS!)")

        teases = [
            "Don't be shy.",
            "Afraid, are ya?",
            "Coward.",
            "Come oooonnnnn.",
            "You're not getting out of this",
            "Where's your funny bone?",
        ]

        nickname = ""

        while nickname == "":
            unsafe_nickname = input().strip().strip(string.punctuation)
            symbols = "!@#$%^&*()-+?_=,<>/;:"

            if unsafe_nickname == "":
                print(random.choice(teases) + " Try Again.\n")

            elif unsafe_nickname.isnumeric():
                print("Name cannot be a number. Try Again.\n")

            elif any(char in symbols for char in unsafe_nickname):
                print("Name cannot include special symbols. Try Again\n")

            else:
                nickname = unsafe_nickname

        file = "high_scores/"

        if self.wordlength == 4:
            file += "squadrant_scores.txt"
        elif self.wordlength == 5:
            file += "5wordle_scores.txt"
        elif self.wordlength == 7:
            file += "rule_of_7_scores.txt"

        with open(file, "a") as scoreboard:
            scoreboard.write(f"{nickname}: {self.score}\n")

        print(f"{nickname}, You're on the board!\n")
