# PARENT CLASS ---------------------------------------------------- #
class Game:
    colors = [  # name, rgb_code
        ("white", "#FFFFFF"),
        ("black", "#000000"),
        ("red", ""),
        ("light_red", ""),
        ("dark_red", ""),
        ("green", ""),
        ("light_green", ""),
        ("dark_green", ""),
        ("blue", ""),
        ("light_blue", ""),
        ("dark_blue", ""),
    ]
    
    def __init__(self) -> None:
        self.is_running: bool = False
        self.started: str = ""
        self.stoped: str = ""
        self.player = Human()
        self.database = Database()
    
    def start(self) -> None:
        self.clear_cmd()
        print("Welcome to the Number Guessing game!")
        print("I'm thinking of the number between 1 and 100.")
        print("You need to guess the number.\n")
        self.is_running = True
        self.started = strftime("%Y-%m-%d %H:%M:%S")
        while self.is_running:
            self.round = Round(self.player, self.database)
            self.round.start()
            self.ask_stop()
        
    def ask_stop(self) -> None:
        while True:
            print("Do you want to quit game? Y / n?")
            print("Enter your choice: ", end="")
            answer = input()
            if self.is_valid_answer(answer):
                break
        if answer == "y":
            self.clear_cmd()
            self.stop()
        else:
            self.clear_cmd()
            print("Welcome to the Number Guessing game!")
            print("I'm thinking of the number between 1 and 100.")
            print("You need to guess the number.\n")

    def stop(self) -> None:
        print("Thank you for playing!")
        print("See you soon!")
        self.stoped = strftime("%Y-%m-%d %H:%M:%S")
        self.is_running = False
        self.save_data()
        sleep(3)
        self.clear_cmd()

    def is_ran_out_attempts(self) -> bool:
        if self.round.attempts > self.difficulties[self.selected_difficulty]["attempts"]:
            print("You've ran out of attempts!")
            return True
        else:
            return False
    
    def save_data(self) -> None:
        pass
    
    @staticmethod
    def clear_cmd() -> None:
        system("cls" if name == "nt" else "clear")
            
    @staticmethod
    def is_valid_answer(answer) -> bool:
        if answer.lower() in "yn":
            return True
        else:
            print('You should write a keyword: "y" or "n".')
            return False
        

if __name__ == "__main__":
    pass
else:
    from time import strftime, sleep
    from os import system, name
    
    from classes.player import Human
    from classes.database import Database
    from classes.round import Round
    