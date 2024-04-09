import string
import art

class Round():
    """A round of Wordle"""

    def __init__(self, answer, wordlength, max_guesses) -> None:
        self.answer = answer
        self.wordlength = wordlength
        self.max_guesses = max_guesses

    def play_round(self) -> str:
        """ Main game loop """
        print(art.logo)

        for i in range(1, self.max_guesses+1):
            guess = self.get_guess(i)
            if self.process_guess(guess):
                print()
            else:
                break
        
        if guess.lower() != self.answer:
            print(art.lost)
            print(f"You lost. The Answer was: {self.answer}")

    def get_guess(self, current_turn) -> str:
        """Gets a guess from the player and checks it"""

        guess = ""
        
        while guess == "":
            print(f"{current_turn} / {self.max_guesses}")
            print("Enter Guess:")
            unsafe_guess = input()

            if len(unsafe_guess.strip().strip(string.punctuation)) == self.wordlength and not unsafe_guess.isnumeric():
                guess = unsafe_guess.lower()
            elif unsafe_guess.isnumeric():
                print("Guess cannot be a number. Try again.\n")
            else:
                print(f"Guess has to be {self.wordlength} letters long. Try again.\n")
        
        return guess

    def process_guess(self, guess):
        """Analyzes the guess from the player and shows status"""

        if guess.lower() == self.answer:
            print(art.celebration)
            print(f"The self.answer is {self.answer}")
            return False

        else:
            show_string = ["-"]*self.wordlength

            for i in range(self.wordlength):
                if guess[i] == self.answer[i]:
                    show_string[i] = "C"
                elif guess[i] in self.answer:
                    show_string[i] = "c"

            print("".join(show_string))
            return True
