class Round():
    difficulties = [  # name, key, attempts
        ("easy", "1", 10),
        ("medium", "2", 5),
        ("hard", "3", 3),
    ]
    
    def __init__(self, player, database) -> None:
        self.is_running: bool = False
        self.started: str = ""
        self.stoped: str = ""
        self.round: int = 0
        self.difficulty: int = 0
        self.player = player
        self.database = database
        
    def start(self) -> None:
        self.is_running = True
        while self.is_running:
            self.ask_difficulty()
            self.started = strftime("%Y-%m-%d %H:%M:%S")
            self.round += 1
            self.player.round = self.round
            print(f"Let's start round #{self.round}!\n")
            self.generator = Generator()
            self.generator.generate_random_number()
            while not self.player.is_guessed():
                self.player.presume_number(self.generator.number)
                if self.player.is_ran_out_attempts(self.difficulties[self.difficulty - 1][2]):
                    break
            self.ask_restart()
            
    def ask_restart(self) -> None:
        while True:
            print("Start a new round? Y / n?")
            print("Enter your choice: ", end="")
            answer = input()
            self.clear_cmd()
            if self.is_valid_answer(answer):
                break
        if answer == "n":
            self.stop()
        
    def stop(self) -> None:
        self.is_running = False
        self.stoped = strftime("%Y-%m-%d %H:%M:%S")
        
    def ask_difficulty(self) -> None:
        while True:
            print(f"Select the difficulty level:")
            print(f"1. Easy (10 attempts)")
            print(f"2. Medium (5 attempts)")
            print(f"3. Hard (3 attempts)")
            print()
            print(f"Enter your choise: ", end="")
            self.difficulty: int = input()
            self.clear_cmd()
            if self.is_valid_difficulty():
                break
        print(f"Your difficulty level is {self.difficulties[self.difficulty - 1][0]}.")
    
    def is_valid_difficulty(self) -> bool:
        # type
        try:
            self.difficulty = int(self.difficulty)
        except ValueError:
            print("You should enter a number.")
            print()
            return False
        # range
        if not (1 <= self.difficulty <= 3):
            print("You should enter a number from 1 to 3.")
            print()
            return False
        else:
            return True
        
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
    from os import system, name
    from time import strftime
    
    from classes.generator import Generator