class Profile:
    def __init__(self, name, wordle = 0, ro7 = 0, squad = 0) -> None:
        self.name = name
        self.wordle_score = wordle
        self.ro7_score = ro7
        self.squad_score = squad
        self.total_wins = 0
        self.total_losses = 0

    def __str__(self):
        ret_string = f"{self.name} {" " * (10-len(self.name))} \t\t {self.wordle_score} \t\t {self.ro7_score} \t\t {self.squad_score} \t\t {self.total_wins} \t\t {self.total_losses}"
        return ret_string

class Profile_Manager:
    def __init__(self) -> None:
        self.profiles = []

    def get_profiles(self):

        file_names = ["high_scores/5wordle_scores.txt", "high_scores/rule_of_7_scores.txt", "high_scores/squadrant_scores.txt"]
        for i in range(3):
            with open(file_names[i]) as file:
                data = file.read().splitlines()
        
            for line in data:
                line = line.split(":")
                line[0] = line[0].strip()
                line[1] = int(line[1])

                find_profile = self.find_profile(line[0])

                if find_profile:
                    if i == 0:
                        if find_profile.wordle_score < line[1]:
                            find_profile.wordle_score = line[1]
                    elif i == 1:
                        if find_profile.ro7_score < line[1]:
                            find_profile.ro7_score = line[1]
                    elif i == 2:
                        if find_profile.squad_score < line[1]:
                            find_profile.squad_score = line[1]
                    
                    if line[1] != 0:
                        find_profile.total_wins += 1
                    else:
                        find_profile.total_losses += 1

                else:
                    new_profile = Profile(name = line[0])
                    if i == 0:
                        new_profile.wordle_score = line[1]
                    elif i == 1:
                        new_profile.ro7_score = line[1]
                    elif i == 2:
                        new_profile.squad_score = line[1]

                    if line[1] != 0:
                        new_profile.total_wins += 1
                    else:
                        new_profile.total_losses += 1

                    self.profiles.append(new_profile)

    def find_profile(self, name):
        for profile in self.profiles:
            if profile.name == name:
                return profile
        return None
    
    def sort_profiles(self):
        sorted_list = sorted(self.profiles, key=lambda profile: profile.name)
        self.profiles = sorted_list

    def print_profiles(self):
        if self.profiles:
            self.sort_profiles()
            print("NAME \t\t\t WORDLE \t RULE OF 7 \t SQUADRANT \t TOTAL WINS \t TOTAL LOSSES")
            print("-"*103)
            [print(prof) for prof in self.profiles]
        else:
            print("No profiles exist yet.")
