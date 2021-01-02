import random
from .player import Player

""" TaylorPlayer by picks moves that already match
 numbers currently in play, with a bias toward moves that
 are 2x on the same number. It stops when all 3 numbers are in play """
class TaylorPlayer(Player):
    def __init__(self, name):
        super(TaylorPlayer, self).__init__(name)

    def get_random_number(self):
        # A new function that the parent class doesn't have! I can use this internally
        return random.randint(1, 2)

    """ cur_num_count is how many numbers are currently being played (0-3)"""
    def how_many_numbers_changed(self, changes):
        cur_num_count = 0
        for key in changes.keys():
            if key == 'turn':
                continue
            if changes[key] > 0:
                cur_num_count += 1
        return cur_num_count

    """ cur_num is just a list of the currently-playing numbers """
    def which_numbers_changed(self, changes):
        cur_num = []
        for key in changes.keys():
            if key == 'turn':
                continue
            if changes[key] > 0:
                num = int(key)
                cur_num.append(num)
        return cur_num

    """ best moves is a dictionary of moves and how strongly they match the
    already-playing numbers. Extra point for if it's 2 of the same number
    NOTE: the key of best_moves is the _index_ for the move in the moves list"""
    def best_matched_moves(self, cur_num, moves):
        best_moves = {}
        for move in moves:
            num_match = 0
            for option in move:
                if(option in cur_num):
                    num_match += 1
            # if the move is 2 of the same number, stronger match
            if((len(move) > 1) and (move[0] == move[1])):
                num_match += 1
            best_moves[moves.index(move)] = num_match

        return best_moves

    def is_continuing_turn(self, board, changes):
        cur_num_count = self.how_many_numbers_changed(changes)
        return cur_num_count < 3 # we keep going until we use all 3 of our numbers, then stop

    def choose_move(self, moves, board, changes, invalid_move=False):
        cur_num = self.which_numbers_changed(changes)
        best_moves = self.best_matched_moves(cur_num, moves)

        # searches through the best_moves dictionary to find the highest ranked move
        return_move = [0,0] #[move index, move score]
        for move in best_moves.keys():
            if best_moves[move] > return_move[1]:
                return_move = [move, best_moves[move]]

        # Always selects the first available move
        return moves[return_move[0]]
