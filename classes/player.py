class Player:
    def __init__(self) -> None:
        self.round: int = 0
        self.attempt: int = 0
        self.generated_number: int = 0
        self.number: int = 0
        self.presumed_numbers: list = []
    
    def is_valid_number(self) -> bool:
        # type
        try:
            self.number = int(self.number)
        except ValueError:
            print("You should enter a number.")
            return False
        # range
        if not (1 <= self.number <= 100):
            print("Number should be in range from 1 to 100.")
            return False
        else:
            return True
    
    def are_equal_numbers(self) -> bool:
        if self.generated_number == self.number:
            return True
        else:
            return False
        
    def is_generated_number_greater(self) -> bool:
        if self.generated_number > self.number:
            return True
        else:
            return False
    
    def is_generated_number_less(self) -> bool:
        if self.generated_number < self.number:
            return True
        else:
            return False
        
    def is_guessed(self) -> bool:
        if not self.attempt == 0:
            if self.is_generated_number_less():
                print("Incorrect!")
                print(f"My number is less than {self.number}.")
                print()
                return False
            elif self.is_generated_number_greater():
                print("Incorrect!")
                print(f"My number is greater than {self.number}.")
                print()
                return False
            elif self.are_equal_numbers():
                print("Congratulations!")
                print(f"You guessed the number in {self.attempt} attempts.")
                print()
                self.attempt = 0
                self.presumed_numbers = []
                return True
        
    def is_ran_out_attempts(self, attempts) -> bool:
        if self.attempt >= attempts:
            print("You're ran out of attempts!")
            print()
            self.attempt = 0
            self.presumed_numbers = []
            return True
        else:
            return False
        
    @staticmethod
    def clear_cmd() -> None:
        system("cls" if name == "nt" else "clear")
        
    def presume_number(self) -> None:
        pass
        

class Human(Player):
    def __init__(self) -> None:
        super().__init__()
        
    def presume_number(self, generated_number) -> None:
        self.generated_number = generated_number
        while True:
            self.attempt += 1
            print(f"Round: {self.round}. Attempt: {self.attempt}")
            print(f"Presumed: ", end="")
            [print(f"{n}, ", end="") for n in self.presumed_numbers]
            print()
            print(f"Enter your guess: ", end="")
            self.number:int = input()
            self.clear_cmd()
            if self.is_valid_number():
                break
        self.presumed_numbers.append(self.number)


class Computer(Player):
    def __init__(self) -> None:
        super().__init__()


if __name__ == "__main__":
    pass
else:
    from os import system, name
