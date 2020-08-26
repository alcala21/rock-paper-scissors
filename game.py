import random


class Rps:
    def __init__(self):
        self.beat = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}

    def play(self):
        while True:
            user = input()
            computer = random.choice(list(self.beat.keys()))
            if computer == user:
                print(f"There is a draw ({computer})")
            elif computer == self.beat.get(user, ""):
                print(f"Sorry, but the computer chose {computer}")
            elif self.beat[computer] == user:
                print(f"Well done. The computer chose {computer} and failed.")
            elif user == '!exit':
                print("Bye!")
                break
            else:
                print("Invalid input")


game = Rps()
game.play()
