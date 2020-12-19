class ColumnFinishedError(Exception):
    pass


class PlayerNotFoundError(Exception):
    pass


class Player:
    def __init__(self, name):
        self.name = name
        self.active_columns = []
        self.finished_columns = []
        self.is_active = False

    def did_win(self):
        return len(self.finished_columns) == 3

    def can_move(self, column):
        return self.is_active and \
            (column in self.active_columns or
             len(self.active_columns) < 3)

    def start_turn(self):
        self.is_active = True

    def end_turn(self):
        self.is_active = False

    def json(self):
        return {
            'name': self.name,
            'active_columns': self.active_columns,
            'finished_columns': self.finished_columns,
            'is_active': self.is_active
        }

    def __str__(self):
        return '<Player::{}, active={}, active_columns={}, finished_columns={}>'.format(
            self.name, self.is_active, self.active_columns,
            self.finished_columns)


class Column:
    def __init__(self, value, steps, players):
        self.value = value
        self.steps = steps
        self.states = {}
        for player in players:
            self.states[player] = 0
        self.is_finished = False

    def can_move_player(self, player):
        return not self.is_finished and \
            player in self.states and \
                self.states[player] < self.steps

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
        if not self.can_move_player(player) and not self.is_finished:
            raise PlayerNotFoundError
        if not self.can_move_player(player):
            raise ColumnFinishedError

        self.states[player] += steps
        self.check_for_finished()

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
            return 'Column {} finished by player {}'.format(self.get_leaders()[0])
        result = 'Column {} player positions:\n'
        for state in self.get_leaderboard():
            result += '{} has completed {} of {} steps.\n'.format(
                state[0], state[1], self.steps)
        return result


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
        self.players = { name: Player(name) for name in names }

    def can_move_player(self, name, col):
        return self.players[name].can_move(col) and \
            self.columns[col].can_move_player(name)

    def json(self):
        return {
            'columns': { c: self.columns[c].json() for c in self.columns.keys() },
            'players': { p: self.players[p].json() for p in self.players.keys() }
        }
