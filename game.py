import random

class Rps:
    def __init__(self):
        self.beat = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}

    def play(self):
        user = input()
        print(f"Sorry, but the computer chose {self.beat[user]}")


game = Rps()
game.play()
