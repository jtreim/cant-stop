import random

from errors import GameNotReadyError
from game import CantStop

from example_player import DumbPlayer
from player import Player


class Tournament:
    MIN_MATCHES = 100

    def __init__(self, verbose=False):
        self.game = None
        self.players = []
        self.stats = {}
        self.verbose = verbose

    def add_player(self, player_name, player_class):
        self.players.append((player_name, player_class))
        self.stats[player_name] = {
            'total_matches': 0,
            'matches_won': 0,
            'win_rate': 0,
            'columns_finished': 0,
            'turns_dropped': 0,
            'missed_steps': 0
        }

    def get_random_players(self, num_players):
        available = self.players.copy()
        random.shuffle(available)
        players = []
        for i in range(num_players):
            players.append(available[i])
        return players

    def setup_match(self, players=None):
        # Can't start match without at least 2 players
        if len(self.players) < 2:
            return False

        # Randomly decide on players if not specified otherwise
        if players is None:
            players = self.get_random_players(3)        

        self.game = CantStop(player_classes=players, verbose=self.verbose)

    def run_match(self):
        if self.game is None:
            raise GameNotReadyError
        results = self.game.play_game()
        for key in results.keys():
            self.stats[key]['total_matches'] += 1
            if len(results[key]['finished']) >= 3:
                self.stats[key]['matches_won'] += 1
            self.stats[key]['win_rate'] = \
                self.stats[key]['matches_won'] / self.stats[key]['total_matches']
            self.stats[key]['columns_finished'] += len(results[key]['finished'])
            self.stats[key]['turns_dropped'] += results[key]['turns_dropped']
            self.stats[key]['missed_steps'] += results[key]['steps_dropped']['total']

    def run(self):
        for i in range(self.MIN_MATCHES):
            self.setup_match()
            self.run_match()
        print('-------------------- RESULTS --------------------')
        for key in self.stats.keys():
            print('Player: {}'.format(key))
            print('Total Matches: {}'.format(self.stats[key]['total_matches']))
            print('Matches Won: {}'.format(self.stats[key]['matches_won']))
            print('Win Rate: {}%'.format(100 * self.stats[key]['win_rate']))
            print('Columns Finished: {}'.format(self.stats[key]['columns_finished']))
            print('Turns Dropped: {}'.format(self.stats[key]['turns_dropped']))
            print('Steps Dropped: {}'.format(self.stats[key]['missed_steps']))
            print()


if __name__ == '__main__':
    tournament = Tournament()
    tournament.add_player('Base', Player)
    tournament.add_player('Dumb', DumbPlayer)
    tournament.add_player('Another Base', Player)
    tournament.run()
