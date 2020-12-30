import random

class Player:
    def __init__(self, name):
        self.name = name

    def is_continuing_turn(self, board, changes):
        """
        board: Dictionary containing board information
               Example: {
                    '2': {
                        'value': 2,
                        'steps': 3,
                        'players': [('Cameron', 1), ('Jeff', 0), ('Taylor', 1)],
                    },
                    '3': {
                        'value': 3,
                        'steps': 5,
                        'players': [('Cameron', 0), ('Jeff', 1), ('Taylor', 0)],
                    },
                    '4': {
                        'value': 4,
                        'steps': 7,
                        'players': [('Cameron', 4), ('Jeff', 0), ('Taylor', 3)],
                    },
                    '5': {
                        'value': 5,
                        'steps': 9,
                        'players': [('Cameron', 4), ('Jeff', 0), ('Taylor', 4)],
                    },
                    '6': {
                        'value': 6,
                        'steps': 11,
                        'players': [('Cameron', 9), ('Jeff', 9), ('Taylor', 2)],
                    },
                    '7': {
                        'value': 7,
                        'steps': 13,
                        'players': [('Cameron', 1), ('Jeff', 0), ('Taylor', 2)],
                    },
                    '8': {
                        'value': 8,
                        'steps': 11,
                        'players': [('Cameron', 1), ('Jeff', 0), ('Taylor', 2)],
                    },
                    '9': {
                        'value': 9,
                        'steps': 9,
                        'players': [('Cameron', 1), ('Jeff', 0), ('Taylor', 2)],
                    },
                    '10': {
                        'value': 10,
                        'steps': 7,
                        'players': [('Cameron', 1), ('Jeff', 0), ('Taylor', 2)],
                    },
                    '11': {
                        'value': 11,
                        'steps': 5,
                        'players': [('Cameron', 3), ('Jeff', 3), ('Taylor', 5)],
                    },
                    '12': {
                        'value': 12,
                        'steps': 3,
                        'players': [('Cameron', 1), ('Jeff', 0), ('Taylor', 2)],
                    }
                }
 
        changes: Dictionary with all the changes since the turn began
                 Example: {
                    'turn': 1,
                    '2': 0,
                    '3': 2,
                    '4': 2,
                    '5': 0,
                    '6': 0,
                    '7': 0,
                    '8': 0,
                    '9': 0,
                    '10': 0,
                    '11': 0,
                    '12': 1
                 }
 
        Returns: boolean stating whether the player will roll again or not
        """
        return not (random.randint(1, 6) == 1)

    def choose_move(self, moves, board, changes, invalid_move=False):
        """
        Submits action for the game
 
        moves: List of available moves for the player to choose from.
               Example: [[5, 8], [6], [7], [4], [9]]
                        (In the situation where the player rolled 1, 3, 4, & 5, has columns 5 & 8 started).
 
        board: Dictionary containing board information
               Example: {
                    '2': {
                        'value': 2,
                        'steps': 3,
                        'players': [('Cameron', 1), ('Jeff', 0), ('Taylor', 1)],
                    },
                    '3': {
                        'value': 3,
                        'steps': 5,
                        'players': [('Cameron', 0), ('Jeff', 1), ('Taylor', 0)],
                    },
                    '4': {
                        'value': 4,
                        'steps': 7,
                        'players': [('Cameron', 4), ('Jeff', 0), ('Taylor', 3)],
                    },
                    '5': {
                        'value': 5,
                        'steps': 9,
                        'players': [('Cameron', 4), ('Jeff', 0), ('Taylor', 4)],
                    },
                    '6': {
                        'value': 6,
                        'steps': 11,
                        'players': [('Cameron', 9), ('Jeff', 9), ('Taylor', 2)],
                    },
                    '7': {
                        'value': 7,
                        'steps': 13,
                        'players': [('Cameron', 1), ('Jeff', 0), ('Taylor', 2)],
                    },
                    '8': {
                        'value': 8,
                        'steps': 11,
                        'players': [('Cameron', 1), ('Jeff', 0), ('Taylor', 2)],
                    },
                    '9': {
                        'value': 9,
                        'steps': 9,
                        'players': [('Cameron', 1), ('Jeff', 0), ('Taylor', 2)],
                    },
                    '10': {
                        'value': 10,
                        'steps': 7,
                        'players': [('Cameron', 1), ('Jeff', 0), ('Taylor', 2)],
                    },
                    '11': {
                        'value': 11,
                        'steps': 5,
                        'players': [('Cameron', 3), ('Jeff', 3), ('Taylor', 5)],
                    },
                    '12': {
                        'value': 12,
                        'steps': 3,
                        'players': [('Cameron', 1), ('Jeff', 0), ('Taylor', 2)],
                    }
                }
  
        changes: Dictionary with all the changes since the turn began
                 Example: {
                    'turn': 1,
                    '2': 0,
                    '3': 2,
                    '4': 2,
                    '5': 0,
                    '6': 0,
                    '7': 0,
                    '8': 0,
                    '9': 0,
                    '10': 0,
                    '11': 0,
                    '12': 1
                 }

        invalid_move: A boolean flag stating whether the last submitted move was determined invalid.

        Returns: one of the moves in the list
        """
        idx = random.randrange(0, len(moves))
        return moves[idx]

    def json(self):
        return {
            'name': self.name,
        }

    def __str__(self):
        return '<Player::{}>'.format(self.name)
