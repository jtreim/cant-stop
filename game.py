import random

from errors import (
    ColumnFinishedError, PlayerNotFoundError, BoardMissingError,
    NotEnoughPlayersError, InvalidMoveError)

from player import Player
from board import Board


class CantStop:
    MAX_MOVE_ATTEMPTS = 3
    END_TURN = 'end_turn'

    def __init__(self, player_classes=None, verbose=False):
        self.players = {}
        self.player_classes = player_classes
        self.names = []
        self.board = None
        self.is_finished = False
        self.finished_columns = {}
        self.active_columns = []
        self.dropped_steps = {}
        self.turns_taken = {}
        self.verbose = verbose

        # Set order for turns to be taken
        # Current turn is an index into turn order
        self.turn_order = []
        self.current_turn = 0
        if self.player_classes is not None:
            self.reset(self.player_classes)
        else:
            self.names = []

        # Log for all moves that occur throughout the course of the game
        self.log = []

    def log_entry(self, msg):
        self.log.append(msg)
        if self.verbose:
            print(msg)

    def add_player(self, name):
        # Enforce unique player names
        if name in self.names:
            return False
        self.names.append(name)
        self.reset(self.names)
        return True

    def remove_player(self, name):
        try:
            self.names.remove(name)
        except ValueError:
            return False
        return True

    def reset(self, player_classes=None):
        # player_classes: List of tuples containing player classes and their names
        self.board = Board(names)
        self.is_finished = False
        self.current_turn = 0
        self.finished_columns = {}
        self.dropped_steps = {}
        self.turns_taken = {}
        self.player_classes = player_classes
        self.names = []
        if self.player_classes is not None:
            for tup in self.player_classes:
                player_class = tup[0]
                player_name = tup[1]
                self.players[player_name] = player_class(player_name)
                self.names.append(player_name)
            self.turn_order = self.names.copy()
            self.finished_columns = { name: [] for name in self.names }
            self.dropped_steps = { name: {
                'total': 0,
                'individual': self.get_default_changes()
            } for name in self.names }
            self.turns_taken = { name: 0 for name in self.names }
            random.shuffle(self.turn_order)

    def get_roll(self):
        rolls = []
        for i in range(4):
            rolls.append(random.randint(1, 6))
        return rolls

    def get_moves_from_roll(self, rolls):
        # Determine possible moves from a dice roll
        moves = []
        moves.append([rolls[0] + rolls[1], rolls[2] + rolls[3]])
        moves[-1].sort()
        moves.append([rolls[0] + rolls[2], rolls[1] + rolls[3]])
        moves[-1].sort()
        moves.append([rolls[0] + rolls[3], rolls[1] + rolls[2]])
        moves[-1].sort()
        return moves

    def remove_duplicate_moves(self, moves):
        # Remove any duplicate moves
        result = []
        for move in moves:
            if move not in result:
                result.append(move)
        return result

    def remove_finished_column_moves(self, moves):
        # Remove moves that advance on a finished column
        result = []
        for move in moves:
            result.append([m for m in move if m not in self.board.get_finished_columns()])
        return result

    def remove_new_column_moves(self, moves):
        # Remove moves that activate new columns if player can't activate more
        result = []
        for move in moves:
            result.append([i for i in move if i in self.active_columns])
        return result

    def split_new_column_moves(self, moves):
        # Split moves if player can only add one more column
        result = []
        for move in moves:
            has_active_column = False
            for col in move:
                if col in self.active_columns:
                    has_active_column = True
                    break
            if has_active_column:
                result.append(move)
            else:
                for col in move:
                    result.append([col])
        return result

    def get_moves(self, roll):
        moves = self.get_moves_from_roll(roll)
        moves = self.remove_finished_column_moves(moves)
        if len(self.active_columns) == 3:
            moves = self.remove_new_column_moves(moves)
        elif len(self.active_columns) == 2:
            moves = self.split_new_column_moves(moves)
        moves = self.remove_duplicate_moves(moves)
        moves = [m for m in moves if m != []]
        if len(moves) == 0:
            moves.append(self.END_TURN)
        return moves

    def print_log(self):
        return '\n'.join(self.log)

    def check_for_finished(self):
        finished = False
        for name in self.names:
            if len(self.finished_columns[name]) >= 3:
                finished = True
                break
        self.is_finished = finished

    def get_results(self):
        if not self.is_finished:
            return None
        results = {}
        for name in self.names:
            results[name] = {}
            results[name]['finished'] = self.finished_columns[name]
            results[name]['steps_dropped'] = self.dropped_steps[name]
        return results

    def execute_move(self, name, player_move, changes):
        if player_move == self.END_TURN:
            self.log_entry(
                '{} saves their progress and ends their turn.'.format(name))
            return changes
        for m in player_move:
            changes[str(m)] += 1
            if m not in self.active_columns:
                self.active_columns.append(m)
            self.log_entry('{} advances on column {}.'.format(name, m))
        return changes

    def get_default_changes(self):
        default = {}
        for i in range(2, 13):
            default[str(i)] = 0
        default['turn'] = 0
        return default

    def make_changes(self, changes, name):
        for key in changes.keys():
            if changes[key] == 0:
                continue
            did_finish = self.board.advance_player(name, key, changes[key])
            if did_finish:
                self.finished_columns[name].append(key)
                self.log_entry('{} has finished column {}'.format(name, key))
                self.check_for_finished()

    def add_missed_steps(self, name, changes):
        for key in changes.keys():
            self.dropped_steps[name]['total'] += changes[key]
            self.dropped_steps[name]['individual'][key] += changes[key]

    def next_turn(self):
        # Get the current player, advance turn tracker to next in line.
        name = self.turn_order[self.current_turn]
        player = self.players[name]
        self.current_turn = (1 + self.current_turn) % len(self.turn_order)
        self.log_entry('{} starts their turn'.format(name))

        # Establish base turn expectations
        self.active_columns = []
        player_move = None
        changes = self.get_default_changes()

        # Let the player continue until they're finished
        while player_move != self.END_TURN:
            changes['turn'] += 1
            self.turns_taken[name] += 1
            roll = self.get_roll()
            self.log_entry('{} rolls {}'.format(name, roll))
            moves = self.get_moves(roll)
            if moves == [self.END_TURN]:
                self.add_missed_steps(name, changes)
                changes = self.get_default_changes()
                self.log_entry('{} cannot advance and ends their turn.'.format(name))
                break

            # Don't let players mutate any moves, board states, or current changes
            player_move = player.choose_move(
                moves.copy(), self.board.json().copy(), changes.copy())
            move_attempts = 0
            while player_move not in moves and \
                    move_attempts < self.MAX_MOVE_ATTEMPTS:
                move_attempts += 1
                player_move = player.choose_move(
                    moves.copy(), self.board.json().copy(), changes.copy(),
                    invalid_move=True)
            
            # Forcibly end turn if player attempts too many invalid moves
            if move_attempts >= self.MAX_MOVE_ATTEMPTS and player_move not in moves:
                self.add_missed_steps(name, changes)
                changes = self.get_default_changes()
                player_move = self.END_TURN
                self.log_entry(
                    '{} tried too many invalid moves, ending their turn.'.format(
                        name))
                continue

            # Add on any changes from the chosen move 
            changes = self.execute_move(name, player_move, changes)
            if not player.is_continuing_turn(self.board.json(), changes.copy()):
                player_move = self.END_TURN
        self.make_changes(changes, name)

    def play_game(self):
        if len(self.turn_order) <= 1:
            raise NotEnoughPlayersError
        if self.board is None:
            raise BoardMissingError

        while not self.is_finished:
            self.next_turn()
        return self.get_results()


def main():
    game = CantStop(names=['Cameron', 'Jeff', 'Taylor'], verbose=True)
    result = game.play_game()
    for key in result:
        print('{}: {}'.format(key, result[key]))


if __name__ == '__main__':
    main()
