import random


class Rps:
    def __init__(self):
        self.beat = {}
        self.options = ['rock', 'paper', 'scissors']
        self.scores = {'draw': 50, 'win': 100, 'lose': 0}
        self.ratings = {}
        self.player = ""

    def play(self):
        self.load_ratings()
        self.select_player()
        self.select_options()

        while True:
            user_input = input()
            computer = random.choice(self.options)

            if computer == user_input:
                print(f"There is a draw ({computer})")
                self.update_rating('draw')

            elif computer in self.beat.get(user_input, ""):
                print(f"Sorry, but the computer chose {computer}")
                self.update_rating('lose')

            elif user_input in self.beat.get(computer, ""):
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

    def select_player(self):
        self.player = input('Enter your name: ')
        print('Hello,', self.player)

        if self.player not in self.ratings:
            self.ratings[self.player] = 0

    def select_options(self):
        option_str = input()
        if option_str == "":
            self.beat = {'rock': ['paper'], 'paper': ['scissors'], 'scissors': ['rock']}
        else:
            self.options = option_str.replace(" ", "").split(",")
            self.make_beat_dict()
        print("Okay, let's start")

    def make_beat_dict(self):
        n_reduced = len(self.options) - 1
        i_beat = n_reduced // 2
        for word in self.options:
            w_index = self.options.index(word)
            new_words = self.options[w_index + 1:] + self.options[:w_index]
            self.beat[word] = new_words[:i_beat]


game = Rps()
game.play()
