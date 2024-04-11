import os
import art
from profile_manager import Profile_Manager


class UIManager:
    def __init__(self) -> None:
        """Empty init for the UIManager"""

        pass

    def show_main_menu(self, title):
        """UI for Main Menu"""

        self.clear_screen()
        print(art.logo)
        print(title + "\n")
        print("1. Play Wordle")
        print("2. See scoreboards")
        print("3. See profiles")
        print("4. Add word to wordlist")
        print("5. Remove word from wordlist")
        print("\nPress any other button to quit")
        choice = input("(1 / 2 / 3 / 4 / 5): ")
        return choice

    def game_mode(self):
        """UI for Game Mode selection"""

        self.clear_screen()
        print(art.game_mode)
        print("Pick Game Mode:")
        print("1. Normal\n\t5 letter word, 5 guesses\n")
        print("2. Squadrant\n\t4 letter word, 6 guesses\n")
        print("3. Rule of 7\n\t7 letter word, 7 guesses\n")
        mode = input("(1 / 2 / 3):\n")
        return mode

    def see_scoreboards(self):
        """UI to choose a scoreboard"""

        self.clear_screen()
        print(art.scoreboard)
        print("Choose scoreboard")
        print("1. Normal Mode")
        print("2. Squadrant")
        print("3. Rule of 7")
        print("(1 / 2 / 3):")
        choice = input()
        return choice

    def see_specified_scoreboard(self, scoreboard, title, number_of_lines):
        """UI for Specified scoreboard"""

        # clear screen and show UI
        self.clear_screen()
        print(art.scoreboard)
        print(" -- " + title + " -- ")

        # Check there is any data in the file
        if number_of_lines == 0:
            print("No data available for this game mode\n")
            input("Press Enter to quit")

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

            input("\nPress Enter to quit\n")

    def see_profiles(self):
        """UI to see profiles"""

        self.clear_screen()
        print(art.profiles)

        pf = Profile_Manager()
        pf.get_profiles()
        pf.print_profiles()
        print("\n*Note that only the highest score of each user is shown.")
        print("For further details, see High Scores page")
        input("\nPress enter to quit\n")

    def add_remove_word(self, operation):
        """UI to add or remove a word"""

        self.clear_screen()
        print(art.settings)
        print(f"First enter the length of the word that you want to {operation}")
        print("(Must be 4, 5, or 7)")

    def play_round(self):
        os.system("cls" if os.name == "nt" else "clear")
        print(art.logo)
        print("Previous Guesses")
        print("-----------------")

    def lose_game(self, answer):
        print(art.lost)
        print(f"You lost. The Answer was: {answer}")

    def win_game(self, answer):
        print(art.celebration)
        print(f"The answer is {answer}")

    def print_previous_guesses(self, guesses):
        top_line = "| "
        bottom_line = "| "
        for guess in guesses:
            top_line += guess[0] + " | "
            bottom_line += guess[1] + " | "

        print(top_line)
        print(bottom_line)
        print()

    def clear_screen(self):
        """Clears the screen"""

        os.system("cls" if os.name == "nt" else "clear")
