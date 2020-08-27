import random


class Rps:
    def __init__(self):
        self.beat = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
        self.scores = {'draw': 50, 'win': 100, 'lose': 0}
        self.ratings = {}
        self.player = ""
        self.load_ratings()

    def play(self):
        self.player = input('Enter your name: ')
        print('Hello,', self.player)

        if self.player not in self.ratings:
            self.ratings[self.player] = 0

        while True:
            user_input = input()
            computer = random.choice(list(self.beat.keys()))

            if computer == user_input:
                print(f"There is a draw ({computer})")
                self.update_rating('draw')

            elif computer == self.beat.get(user_input, ""):
                print(f"Sorry, but the computer chose {computer}")
                self.update_rating('lose')

            elif self.beat[computer] == user_input:
                print(f"Well done. The computer chose {computer} and failed.")
                self.update_rating('win')

            elif user_input == '!exit':
                print("Bye!")
                break

            elif user_input == '!rating':
                print("Your rating:", self.ratings[self.player])

            else:
                print("Invalid input")

    def update_rating(self, result):
        self.ratings[self.player] += self.scores[result]

    def load_ratings(self):
        with open('rating.txt', 'r') as r_file:
            for line in r_file.readlines():
                k, v = line.strip().split()
                self.ratings[k] = int(v)


game = Rps()
game.play()
