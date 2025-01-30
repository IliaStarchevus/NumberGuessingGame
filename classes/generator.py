class Generator():
    def __init__(self) -> None:
        self.number: int = 0
        self.generated_at: str = ""
        self.is_guessed: bool = False
        
    def generate_random_number(self, start: int = 1, end: int = 100) -> None:
        """Generating random number in range from start to end (from 1 to 100 as default; both included). Also sets a time when a number was generated"""
        self.number = randint(start, end)
        self.generated_at = strftime("%Y-%m-%d %H:%M:%S")
        return self.number
    
if __name__ == "__main__":
    pass
else:
    from random import randint
    from time import strftime