"""

"""


class Game:
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print('Help : ...')

    @classmethod
    def show_top_score(cls):
        print(cls.top_score)

    def start_game(self, score):
        # starts game
        print("Starts Game")
        if score > Game.top_score:
            Game.top_score = score


# main logic
Game.show_help()
Game.show_top_score()

# player 1
game1 = Game("Player 1")
game1.start_game(5)
Game.show_top_score()

game1.start_game(10)
Game.show_top_score()


# player 2
game2 = Game("Player 2")
game2.start_game(3)
Game.show_top_score()


game2.start_game(15)
Game.show_top_score()

