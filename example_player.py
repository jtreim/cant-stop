import random
from player import Player

class DumbPlayer(Player):
    def __init__(self, name):
        self.pre_logic = 'I wanna be special, so here\'s an attribute I assign beforehand'
        super(DumbPlayer, self).__init__(name)
        self.post_logic = 'I wanna be extra special, so here\'s another attribute I assign later'

    def get_random_number(self):
        # A new function that the parent class doesn't have! I can use this internally
        return random.randint(1, 2)

    def is_continuing_turn(self, board, changes):
        # Decides to continue turn based on 50% chance the random int is a 1
        return self.get_random_number() == 1

    def choose_move(self, moves, board, changes, invalid_move=False):
        # Always selects the first available move
        return moves[0]
