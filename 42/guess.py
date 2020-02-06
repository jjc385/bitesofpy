import random

MAX_GUESSES = 5
START, END = 1, 20


def get_random_number():
    """Get a random number between START and END, returns int"""
    return random.randint(START, END)


class Game:
    """Number guess class, make it callable to initiate game"""

    def __init__(self):
        """Init _guesses, _answer, _win to set(), get_random_number(), False"""
        self._guesses = set()
        self._answer = get_random_number()
        self._win = False

    def guess(self):
        """Ask user for input, convert to int, raise ValueError outputting
           the following errors when applicable:
           'Please enter a number'
           'Should be a number'
           'Number not in range'
           'Already guessed'
           If all good, return the int"""
        rawInput = self.getInput("Guess a number between 1 and 20")
        try:
            if not isinstance(rawInput, (str, int)):
                raise ValueError("Please enter a number")
            userInt = int(rawInput.strip()) if not isinstance(rawInput, int) else rawInput
            if not START <= userInt <= END:
                raise ValueError("Number not in range")
            if userInt in self._guesses:
                raise ValueError("Already guessed")
            self._guesses.add(userInt)
            return userInt
        except TypeError:
            raise ValueError("Should be a number")

    def getInput(self, prompt=""):
        return input(prompt)

    def _validate_guess(self, guess):
        """Verify if guess is correct, print the following when applicable:
           {guess} is correct!
           {guess} is too low
           {guess} is too high
           Return a boolean"""
        
        if guess == self._answer:
            print(f"{guess} is correct!")
            self._win = True
            return True
        if guess < self._answer:
            print(f"{guess} is too low")
        else:
            print(f"{guess} is too high")
        return False
        

    def __call__(self):
        """Entry point / game loop, use a loop break/continue,
           see the tests for the exact win/lose messaging"""
        nGuesses = 0
        while nGuesses < MAX_GUESSES:
            try:
                guess = self.guess()
                nGuesses += 1
                if self._validate_guess(guess):
                    return
            except ValueError as e:
                print(e.args[0])

        print(f"Guessed {MAX_GUESSES} times, answer was {self._answer}")


if __name__ == '__main__':
    game = Game()
    game()
