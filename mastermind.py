import random
class Game:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.position = []

    def set_up(self, color: int, position: int):
        self.x = color
        self.y = position
        for i in range(position):
            self.position.append(random.randrange(1,color+1))
        print(self.position)
        self.play()

    def play(self):
        round = 0
        while True:
            round += 1
            print(f"Playing mastermind with {self.x} colors and {self.y}"
                  f" positions")
            while True:
                guess = int(input("What is your guess?: "))
                if self.y == len(str(guess)):
                    break
                print("Your number of your guess is not correct")
            print(f"Your guess is {guess}")
            self.show_hint(guess)

    def show_hint(self, guess):
        guess = [int(x) for x in str(guess)]
        guess2 = guess.copy()
        position = self.position.copy()
        hint = []
        for i in range(self.y):
            if self.position[i] == guess[i]:
                hint.append("*")
                position.remove(self.position[i])
                guess2.remove(guess[i])

        for color in position:
            for color_guess in guess2:
                if color == color_guess:
                    hint.append("o")

        for value in hint:
            print(value, end='')
        print()

    def reset(self):
        self.position = []



game1 = Game()
game1.set_up(4,4)
