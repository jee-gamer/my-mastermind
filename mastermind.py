import random


class Game:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.__position = []

    def set_up(self, color: int, position: int):
        if color > 8 or position > 10:
            print("Colors limit is 8 and position limit is 10, try again")
            return
        if color < 0 or position < 0:
            print("Colr and position cannot be negative")
            return
        self.x = color
        self.y = position
        for i in range(position):
            self.__position.append(random.randrange(1,color+1))
        self.play()

    def play(self):
        rounds = 0
        print(f"Playing mastermind with {self.x} colors and {self.y}"
              f" positions")
        while True:
            rounds += 1
            while True:
                guess = input("What is your guess?: ")
                try:
                    guess = int(guess)
                except ValueError as e:
                    print("You must input numbers only\n")

                if self.y == len(str(guess)):
                    break
                print(f"Guess for {self.y} digits, try again\n")
            print(f"Your guess is {guess}")
            guess = [int(x) for x in str(guess)]
            self.show_hint(guess)
            if guess == self.__position:
                print(f"You solve it after {rounds} rounds")
                return

    def show_hint(self, guess):
        guess2 = guess.copy()
        position = self.__position.copy()
        hint = []
        for i in range(self.y):
            if self.__position[i] == guess[i]:
                hint.append("*")
                position.remove(self.__position[i])
                guess2.remove(guess[i])

        for i, color in enumerate(position):
            for j, color_guess in enumerate(guess2):
                if color == color_guess:
                    hint.append("o")
                    position[i] = 0
                    guess2[j] = 0

        for value in hint:
            print(value, end='')
        print("\n")

    def reset(self):
        self.x = 0
        self.y = 0
        self.__position = []

# game1 = Game()
# game1.set_up(4,4)
