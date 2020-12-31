from errors import (
    ColumnFinishedError, PlayerNotFoundError, BoardMissingError,
    NotEnoughPlayersError, InvalidMoveError)

class Column:
    def __init__(self, value, steps, players):
        self.value = value
        self.steps = steps
        self.states = {}
        for player in players:
            self.states[player] = 0
        self.is_finished = False

    def can_move_player(self, player, steps):
        return not self.is_finished and \
            player in self.states and \
                self.states[player] + steps <= self.steps

    def check_for_finished(self):
        is_finished = False
        for player, value in self.states.items():
            if value >= self.steps:
                self.states[player] = self.steps
                is_finished = True
                break
        self.is_finished = is_finished
        return self.is_finished

    def advance_player(self, player, steps=1):
        if player not in self.states:
            raise PlayerNotFoundError
        if not self.can_move_player(player, steps):
            raise ColumnFinishedError

        self.states[player] += steps
        return self.check_for_finished() and steps > 0

    def retreat_player(self, player, steps=1):
        if player not in self.states:
            raise PlayerNotFoundError
    
        self.states[player] -= steps
        if self.states[player] < 0:
            self.states[player] = 0
        self.check_for_finished()

    def get_leaders(self):
        leaders = []
        lead = -1
        for player in self.states.keys():
            if self.states[player] > lead:
                leaders = [player]
                lead = self.states[player]
            elif self.states[player] == lead:
                leaders.append(player)
        return leaders

    def get_leaderboard(self):
        return [(p, v) for p, v in sorted(self.states.items(), key=lambda item: item[1])]  

    def json(self):
        return {
            'value': self.value,
            'steps': self.steps,
            'players': self.get_leaderboard()
        }

    def __str__(self):
        if self.is_finished:
            return '<Column {}::finished by {}>'.format(
                self.value, self.get_leaders()[0])
        result = '<Column {}::positions: '.format(self.value)
        for state in self.get_leaderboard():
            result += '{}: {} of {} steps,'.format(
                state[0], state[1], self.steps)
        return result + '>'


class Board:
    def __init__(self, names):
        self.columns = {
            '2': Column(2, 3, names),
            '3': Column(3, 5, names),
            '4': Column(4, 7, names),
            '5': Column(5, 9, names),
            '6': Column(6, 11, names),
            '7': Column(7, 13, names),
            '8': Column(8, 11, names),
            '9': Column(9, 9, names),
            '10': Column(10, 7, names),
            '11': Column(11, 5, names),
            '12': Column(12, 3, names),
        }

    def get_finished_columns(self):
        finished = []
        for key in self.columns.keys():
            if self.columns[key].is_finished:
                finished.append(int(key))
        return finished

    def can_move_player(self, name, col, steps=1):
        return self.columns[col].can_move_player(name, steps)

    def advance_player(self, name, col, steps):
        return self.columns[col].advance_player(name, steps=steps)

    def json(self):
        return { c: self.columns[c].json() for c in self.columns.keys() }
