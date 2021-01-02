from .player import Player

class JeffPlayer(Player):
    ODDS = 'odds'
    ROLLS = 'rolls'

    ONE_COLUMN_ODDS = {
        '2': { ODDS: .13, ROLLS: 0 },
        '3': { ODDS: .23, ROLLS: 0 },
        '4': { ODDS: .36, ROLLS: 0 },
        '5': { ODDS: .45, ROLLS: 1 },
        '6': { ODDS: .56, ROLLS: 1 },
        '7': { ODDS: .64, ROLLS: 2 },
        '8': { ODDS: .56, ROLLS: 1 },
        '9': { ODDS: .45, ROLLS: 1 },
        '10': { ODDS: .36, ROLLS: 0 },
        '11': { ODDS: .23, ROLLS: 0 },
        '12': { ODDS: .13, ROLLS: 0 },
    }

    TWO_COLUMN_ODDS = {
        '2': {
            '3': { ODDS: .32, ROLLS: 0 },
            '4': { ODDS: .44, ROLLS: 1 },
            '5': { ODDS: .53, ROLLS: 1 },
            '6': { ODDS: .63, ROLLS: 2 },
            '7': { ODDS: .71, ROLLS: 2 },
            '8': { ODDS: .67, ROLLS: 2 },
            '9': { ODDS: .56, ROLLS: 1 },
            '10': { ODDS: .47, ROLLS: 1 },
            '11': { ODDS: .36, ROLLS: 1 },
            '12': { ODDS: .26, ROLLS: 0 },
        },
        '3': {
            '4': { ODDS: .47, ROLLS: 1 },
            '5': { ODDS: .53, ROLLS: 1 },
            '6': { ODDS: .64, ROLLS: 2 },
            '7': { ODDS: .71, ROLLS: 2 },
            '8': { ODDS: .68, ROLLS: 2 },
            '9': { ODDS: .64, ROLLS: 2 },
            '10': { ODDS: .56, ROLLS: 1 },
            '11': { ODDS: .45, ROLLS: 1 },
            '12': { ODDS: .36, ROLLS: 1 },
        },
        '4': {
            '5': { ODDS: .61, ROLLS: 2 },
            '6': { ODDS: .72, ROLLS: 3 },
            '7': { ODDS: .77, ROLLS: 3 },
            '8': { ODDS: .75, ROLLS: 3 },
            '9': { ODDS: .68, ROLLS: 3 },
            '10': { ODDS: .67, ROLLS: 2 },
            '11': { ODDS: .56, ROLLS: 1 },
            '12': { ODDS: .47, ROLLS: 1 },
        },
        '5': {
            '6': { ODDS: .73, ROLLS: 3 },
            '7': { ODDS: .78, ROLLS: 4 },
            '8': { ODDS: .77, ROLLS: 3 },
            '9': { ODDS: .75, ROLLS: 2 },
            '10': { ODDS: .69, ROLLS: 2 },
            '11': { ODDS: .68, ROLLS: 2 },
            '12': { ODDS: .64, ROLLS: 1 },
        },
        '6': {
            '7': { ODDS: .84, ROLLS: 5 },
            '8': { ODDS: .82, ROLLS: 5 },
            '9': { ODDS: .77, ROLLS: 3 },
            '10': { ODDS: .75, ROLLS: 3 },
            '11': { ODDS: .68, ROLLS: 2 },
            '12': { ODDS: .67, ROLLS: 2 },
        },
        '7': {
            '8': { ODDS: .84, ROLLS: 5 },
            '9': { ODDS: .78, ROLLS: 4 },
            '10': { ODDS: .77, ROLLS: 3 },
            '11': { ODDS: .71, ROLLS: 2 },
            '12': { ODDS: .71, ROLLS: 2 },
        },
        '8': {
            '9': { ODDS: .73, ROLLS: 3 },
            '10': { ODDS: .72, ROLLS: 3 },
            '11': { ODDS: .64, ROLLS: 2 },
            '12': { ODDS: .63, ROLLS: 2 },
        },
        '9': {
            '10': { ODDS: .61, ROLLS: 2 },
            '11': { ODDS: .53, ROLLS: 1 },
            '12': { ODDS: .53, ROLLS: 1 },
        },
        '10': {
            '11': { ODDS: .47, ROLLS: 1 },
            '12': { ODDS: .44, ROLLS: 1 },
        },
        '11': {
            '12': { ODDS: .32, ROLLS: 0 }
        },
    }

    THREE_COLUMN_ODDS = {
        '2': {
            '3': {
                '4': { ODDS: .52, ROLLS: 1 },
                '5': { ODDS: .58, ROLLS: 1 },
                '6': { ODDS: .68, ROLLS: 2 },
                '7': { ODDS: .75, ROLLS: 3 },
                '8': { ODDS: .76, ROLLS: 3 },
                '9': { ODDS: .71, ROLLS: 2 },
                '10': { ODDS: .63, ROLLS: 2 },
                '11': { ODDS: .53, ROLLS: 1 },
                '12': { ODDS: .44, ROLLS: 1 },
            },
            '4': {
                '5': { ODDS: .66, ROLLS: 2 },
                '6': { ODDS: .76, ROLLS: 3 },
                '7': { ODDS: .81, ROLLS: 4 },
                '8': { ODDS: .82, ROLLS: 5 },
                '9': { ODDS: .76, ROLLS: 3 },
                '10': { ODDS: .74, ROLLS: 3 },
                '11': { ODDS: .63, ROLLS: 2 },
                '12': { ODDS: .55, ROLLS: 1 },
            },
            '5': {
                '6': { ODDS: .77, ROLLS: 3 },
                '7': { ODDS: .81, ROLLS: 4 },
                '8': { ODDS: .83, ROLLS: 5 },
                '9': { ODDS: .76, ROLLS: 3 },
                '10': { ODDS: .76, ROLLS: 3 },
                '11': { ODDS: .71, ROLLS: 2 },
                '12': { ODDS: .63, ROLLS: 2 },
            },
            '6': {
                '7': { ODDS: .86, ROLLS: 6 },
                '8': { ODDS: .88, ROLLS: 7 },
                '9': { ODDS: .83, ROLLS: 5 },
                '10': { ODDS: .81, ROLLS: 4 },
                '11': { ODDS: .76, ROLLS: 3 },
                '12': { ODDS: .74, ROLLS: 3 },
            },
            '7': {
                '8': { ODDS: .89, ROLLS: 8 },
                '9': { ODDS: .84, ROLLS: 5 },
                '10': { ODDS: .83, ROLLS: 5 },
                '11': { ODDS: .78, ROLLS: 4 },
                '12': { ODDS: .78, ROLLS: 4 },
            },
            '8': {
                '9': { ODDS: .71, ROLLS: 2 },
                '10': { ODDS: .63, ROLLS: 2 },
                '11': { ODDS: .53, ROLLS: 1 },
                '12': { ODDS: .44, ROLLS: 1 },
            },
            '9': {
                '10': { ODDS: .71, ROLLS: 2 },
                '11': { ODDS: .64, ROLLS: 2 },
                '12': { ODDS: .63, ROLLS: 2 },
            },
            '10': {
                '11': { ODDS: .58, ROLLS: 1 },
                '12': { ODDS: .55, ROLLS: 1 },
            },
            '11': {
                '12': { ODDS: .44, ROLLS: 1 },
            },
        },
        '3': {
            '4': {
                '5': { ODDS: .67, ROLLS: 2 },
                '6': { ODDS: .74, ROLLS: 3 },
                '7': { ODDS: .79, ROLLS: 4 },
                '8': { ODDS: .80, ROLLS: 4 },
                '9': { ODDS: .78, ROLLS: 4 },
                '10': { ODDS: .76, ROLLS: 3 },
                '11': { ODDS: .66, ROLLS: 2 },
                '12': { ODDS: .58, ROLLS: 1 },
            },
            '5': {
                '6': { ODDS: .77, ROLLS: 3 },
                '7': { ODDS: .79, ROLLS: 4 },
                '8': { ODDS: .81, ROLLS: 4 },
                '9': { ODDS: .78, ROLLS: 4 },
                '10': { ODDS: .76, ROLLS: 3 },
                '11': { ODDS: .71, ROLLS: 2 },
                '12': { ODDS: .64, ROLLS: 2 },
            },
            '6': {
                '7': { ODDS: .86, ROLLS: 6 },
                '8': { ODDS: .85, ROLLS: 6 },
                '9': { ODDS: .83, ROLLS: 5 },
                '10': { ODDS: .82, ROLLS: 5 },
                '11': { ODDS: .76, ROLLS: 3 },
                '12': { ODDS: .74, ROLLS: 3 },
            },
            '7': {
                '8': { ODDS: .89, ROLLS: 8 },
                '9': { ODDS: .84, ROLLS: 5 },
                '10': { ODDS: .84, ROLLS: 5 },
                '11': { ODDS: .78, ROLLS: 4 },
                '12': { ODDS: .78, ROLLS: 4 },
            },
            '8': {
                '9': { ODDS: .84, ROLLS: 5 },
                '10': { ODDS: .83, ROLLS: 5 },
                '11': { ODDS: .76, ROLLS: 3 },
                '12': { ODDS: .76, ROLLS: 3 },
            },
            '9': {
                '10': { ODDS: .78, ROLLS: 4 },
                '11': { ODDS: .71, ROLLS: 2 },
                '12': { ODDS: .71, ROLLS: 2 },
            },
            '10': {
                '11': { ODDS: .66, ROLLS: 2 },
                '12': { ODDS: .63, ROLLS: 2 },
            },
            '11': {
                '12': { ODDS: .53, ROLLS: 1 },
            },
        },
        '4': {
            '5': {
                '6': { ODDS: .80, ROLLS: 4 },
                '7': { ODDS: .85, ROLLS: 6 },
                '8': { ODDS: .85, ROLLS: 6 },
                '9': { ODDS: .80, ROLLS: 4 },
                '10': { ODDS: .82, ROLLS: 5 },
                '11': { ODDS: .78, ROLLS: 4 },
                '12': { ODDS: .71, ROLLS: 2 },
            },
            '6': {
                '7': { ODDS: .89, ROLLS: 8 },
                '8': { ODDS: .91, ROLLS: 10 },
                '9': { ODDS: .86, ROLLS: 6 },
                '10': { ODDS: .88, ROLLS: 7 },
                '11': { ODDS: .83, ROLLS: 5 },
                '12': { ODDS: .82, ROLLS: 5 },
            },
            '7': {
                '8': { ODDS: .90, ROLLS: 9 },
                '9': { ODDS: .89, ROLLS: 8 },
                '10': { ODDS: .88, ROLLS: 7 },
                '11': { ODDS: .84, ROLLS: 5 },
                '12': { ODDS: .83, ROLLS: 5 },
            },
            '8': {
                '9': { ODDS: .86, ROLLS: 6 },
                '10': { ODDS: .88, ROLLS: 7 },
                '11': { ODDS: .82, ROLLS: 5 },
                '12': { ODDS: .81, ROLLS: 4 },
            },
            '9': {
                '10': { ODDS: .82, ROLLS: 5 },
                '11': { ODDS: .76, ROLLS: 3 },
                '12': { ODDS: .76, ROLLS: 3 },
            },
            '10': {
                '11': { ODDS: .76, ROLLS: 3 },
                '12': { ODDS: .74, ROLLS: 3 },
            },
            '11': {
                '12': { ODDS: .63, ROLLS: 2 },
            },
        },
        '5': {
            '6': {
                '7': { ODDS: .89, ROLLS: 8 },
                '8': { ODDS: .90, ROLLS: 9 },
                '9': { ODDS: .87, ROLLS: 7 },
                '10': { ODDS: .86, ROLLS: 6 },
                '11': { ODDS: .84, ROLLS: 5 },
                '12': { ODDS: .82, ROLLS: 5 },
            },
            '7': {
                '8': { ODDS: .91, ROLLS: 10 },
                '9': { ODDS: .85, ROLLS: 6 },
                '10': { ODDS: .89, ROLLS: 8 },
                '11': { ODDS: .84, ROLLS: 5 },
                '12': { ODDS: .84, ROLLS: 5 },
            },
            '8': {
                '9': { ODDS: .87, ROLLS: 7 },
                '10': { ODDS: .86, ROLLS: 6 },
                '11': { ODDS: .83, ROLLS: 5 },
                '12': { ODDS: .83, ROLLS: 5 },
            },
            '9': {
                '10': { ODDS: .80, ROLLS: 4 },
                '11': { ODDS: .78, ROLLS: 4 },
                '12': { ODDS: .76, ROLLS: 3 },
            },
            '10': {
                '11': { ODDS: .78, ROLLS: 4 },
                '12': { ODDS: .76, ROLLS: 3 },
            },
            '11': {
                '12': { ODDS: .71, ROLLS: 2 },
            },
        },
        '6': {
            '7': {
                '8': { ODDS: .92, ROLLS: 12 },
                '9': { ODDS: .91, ROLLS: 10 },
                '10': { ODDS: .90, ROLLS: 9 },
                '11': { ODDS: .89, ROLLS: 8 },
                '12': { ODDS: .89, ROLLS: 8 },
            },
            '8': {
                '9': { ODDS: .90, ROLLS: 9 },
                '10': { ODDS: .91, ROLLS: 10 },
                '11': { ODDS: .85, ROLLS: 6 },
                '12': { ODDS: .88, ROLLS: 7 },
            },
            '9': {
                '10': { ODDS: .85, ROLLS: 6 },
                '11': { ODDS: .81, ROLLS: 4 },
                '12': { ODDS: .83, ROLLS: 5 },
            },
            '10': {
                '11': { ODDS: .80, ROLLS: 4 },
                '12': { ODDS: .82, ROLLS: 5 },
            },
            '11': {
                '12': { ODDS: .76, ROLLS: 3 },
            },
        },
        '7': {
            '8': {
                '9': { ODDS: .89, ROLLS: 8 },
                '10': { ODDS: .89, ROLLS: 8 },
                '11': { ODDS: .86, ROLLS: 6 },
                '12': { ODDS: .86, ROLLS: 6 },
            },
            '9': {
                '10': { ODDS: .85, ROLLS: 6 },
                '11': { ODDS: .79, ROLLS: 4 },
                '12': { ODDS: .81, ROLLS: 4 },
            },
            '10': {
                '11': { ODDS: .79, ROLLS: 4 },
                '12': { ODDS: .81, ROLLS: 4 },
            },
            '11': {
                '12': { ODDS: .75, ROLLS: 3 },
            },
        },
        '8': {
            '9': {
                '10': { ODDS: .80, ROLLS: 4 },
                '11': { ODDS: .77, ROLLS: 3 },
                '12': { ODDS: .77, ROLLS: 3 },
            },
            '10': {
                '11': { ODDS: .74, ROLLS: 3 },
                '12': { ODDS: .76, ROLLS: 3 },
            },
            '11': {
                '12': { ODDS: .68, ROLLS: 2 },
            },
        },
        '9': {
            '10': {
                '11': { ODDS: .67, ROLLS: 2 },
                '12': { ODDS: .66, ROLLS: 2 },
            },
            '11': {
                '12': { ODDS: .58, ROLLS: 1 },
            },
        },
        '10': {
            '11': {
                '12': { ODDS: .52, ROLLS: 1 },
            },
        },
    }

    NEW_COLUMN_PENALTY = 1
    FINISH_COLUMN_REWARD = 1
    FAVORITE_COLUMN_THRESHOLD = 2/3
    
    CONTESTED_COLUMN = 1

    MY_PROGRESS_MODIFIER = .5
    OPPONENT_PROGRESS_MODIFIER = .5
    STEP_DIVISOR = .08
    ROUGH_ODDS_THRESHOLD = .2
    DESPERATION_TURNS = 2

    def count_finished_columns(self, board, changes):
        count = 0
        leader_progress, my_progress = self.get_progress(board, changes)
        for key in leader_progress.keys():
            if leader_progress['progress'] == 1.0:
                count += 1
        return count

    def get_progress(self, board, changes):
        # Returns progress percentages for leader's & player's progress
        leader_progress = {}
        my_progress = {}
        for key in board.keys():
            leader_progress[key] = {}
            leader = board[key]['players'][0][0]
            lead = board[key]['players'][0][1] / board[key]['steps']
            if leader == self.name:
                leader = board[key]['players'][1][0]
                lead = board[key]['players'][1][1]
            for player in board[key]['players']:
                progress = player[1] / board[key]['steps']
                if lead < progress and player[0] != self.name:
                    leader = player[0]
                    lead = progress
                if player[0] == self.name:
                    my_progress[key] = player[1] + changes[key]
                    my_progress[key] /= board[key]['steps']
            leader_progress[key]['leader'] = leader
            leader_progress[key]['progress'] = lead
        return leader_progress, my_progress

    def get_steps(self, board, changes):
        my_steps = {}
        for key in board.keys():
            for player in board[key]['players']:
                if player[0] == self.name:
                    my_steps[key] = player[1] + changes[key]
        return my_steps

    def get_started_columns(self, changes):
        started = []
        for col in changes.keys():
            if col == 'turn':
                continue
            if changes[col] > 0:
                started.append(col)
        return sorted(started, key=lambda column: int(column))

    def get_finished_columns(self, board, my_progress):
        finished = []
        for key in board.keys():
            for player in board[key]['players']:
                if player[1] == board[key]['steps']:
                    finished.append(key)
            if key not in finished and my_progress[key] == 1:
                finished.append(key)
        return sorted(finished, key=lambda column: int(column))

    def continue_based_on_odds(self, started, turns):
        if len(started) == 3:
            col1, col2, col3 = started[0], started[1], started[2]
            return self.THREE_COLUMN_ODDS[col1][col2][col3][self.ROLLS] > turns
        if len(started) == 2:
            col1, col2 = started[0], started[1]
            return self.TWO_COLUMN_ODDS[col1][col2][self.ROLLS] > turns
        return self.ONE_COLUMN_ODDS[started[0]][self.ROLLS] > turns

    def continue_based_on_new_column(self, board, started, finished, turns):
        # Continues based on chances of getting a new valid column
        base_odds = self.TWO_COLUMN_ODDS[started[0]][started[1]][self.ODDS]
        base_rolls = self.TWO_COLUMN_ODDS[started[0]][started[1]][self.ROLLS]
        available = [col for col in board.keys() if col not in started and col not in finished]
        odds = 0
        for col in available:
            odds += (base_odds * self.ONE_COLUMN_ODDS[col][self.ODDS])

        # Quick and dirty estimation
        new_rolls = (odds - self.ROUGH_ODDS_THRESHOLD) / self.STEP_DIVISOR
        return base_rolls + new_rolls > turns

    def continue_based_on_new_columns(self, board, started, finished, turns):
        # Continues based on chances of getting two new columns
        base_odds = self.ONE_COLUMN_ODDS[started[0]][self.ODDS]
        base_rolls = self.ONE_COLUMN_ODDS[started[0]][self.ROLLS]
        available = [col for col in board.keys() if col not in started and col not in finished]
        odds = 0
        for i in range(len(available)):
            for j in range(i+1, len(available)):
                col1, col2 = available[i], available[j]
                odds += (base_odds * self.TWO_COLUMN_ODDS[col1][col2][self.ODDS])

        # Quick and dirty estimation
        new_rolls = (odds - self.ROUGH_ODDS_THRESHOLD) / self.STEP_DIVISOR
        return base_rolls + new_rolls > turns 

    def opponent_might_win(self, leader_progress):
        opponents = {}
        for col in leader_progress.keys():
            leader = leader_progress[col]['leader']
            if leader == self.name:
                continue
            if leader not in opponents.keys():
                opponents[leader] = 0
            if leader_progress[col]['progress'] == 1.0:
                opponents[leader] += 1
                if opponents[leader] >= 2:
                    return True
        return False

    def started_columns_are_contested(self, board, changes, my_progress, started):
        for col in started:
            players = board[col]['players']
            step_size = 1 / board[col]['steps']
            for player in players:
                if player[0] == self.name:
                    continue

                # Opponent is within 1/3 of my progress, and it's not finished
                if abs(my_progress[col] - player[1] * step_size) <= 1/3 and \
                        my_progress[col] != 1:
                    return True

    def did_finish_column(self, started, my_progress):
        for col in started:
            if my_progress[col] == 1.0:
                return True

    def is_continuing_turn(self, board, changes):
        leader_progress, my_progress = self.get_progress(board, changes)
        started_columns = self.get_started_columns(changes)
        finished_columns = self.get_finished_columns(board, my_progress)

        # No reason to stop before starting 3 columns and none are finished.
        if len(started_columns) < 3 and len(finished_columns) == 0:
            return True

        # Stop if I won
        if len(self.get_my_finished(my_progress)) >= 3:
            return False

        # If I finished a column, let's just end there.
        if self.did_finish_column(started_columns, my_progress):
            return False

        # If I started 3 columns, and I'm not finishing a column,
        # just roll optimal number of times.
        if len(started_columns) == 3:
            return self.continue_based_on_odds(
                started_columns, changes['turn'])

        # Columns are finished, but fewer than 3 columns started
        if len(started_columns) == 2:
            return self.continue_based_on_new_column(
                board, started_columns, finished_columns, changes['turn'])
        elif len(started_columns) == 1:
            return self.continue_based_on_new_columns(
                board, started_columns, finished_columns, changes['turn'])
        
        # Shouldn't ever get here...continuing without starting a column...
        return True

    def determine_move_value(self, move, leader_progress, my_progress, board, started):
        value = 0
        if len(move) == 2 and move[0] != move[1]:
            col1, col2 = str(move[0]), str(move[1])
            value = self.TWO_COLUMN_ODDS[col1][col2][self.ODDS]
        elif len(move) == 2:
            col = str(move[0])
            value = 2 * (self.ONE_COLUMN_ODDS[col][self.ODDS])
        else:
            col = str(move[0])
            value = self.ONE_COLUMN_ODDS[col][self.ODDS]

        unique_columns = set(move)
        for c in unique_columns:
            col = str(c)
            step_size = 1 / board[col]['steps']

            # Reward for finishing a column
            if my_progress[col] + step_size == 1:
                value += self.FINISH_COLUMN_REWARD

            # Penalize for starting new columns
            if str(c) not in started:
                value -= self.NEW_COLUMN_PENALTY

            # Make less likely columns more desirable to move on when 3 columns have started
            if len(started) == 3:
                value += (1 - self.ONE_COLUMN_ODDS[col][self.ODDS])

        return value

    def get_my_finished(self, my_progress):
        finished_columns = []
        for col in my_progress.keys():
            if my_progress[col] == 1:
                finished_columns.append(col)
        return finished_columns

    def look_for_the_win(self, board, my_progress, moves):
        winning_move = None
        finished = self.get_my_finished(my_progress)
        for move in moves:
            columns_finished = 0
            # Consider moving twice on same column
            if len(move) == 2 and move[0] == move[1]:
                col = str(move[0])
                step_size = 2 / board[col]['steps']
                if step_size + my_progress[col] == 1:
                    columns_finished += 1
            else:
                # Otherwise, maybe I can finish two at a time
                for m in move:
                    col = str(m)
                    step_size = 1 / board[col]['steps']
                    if step_size + my_progress[col] == 1:
                        columns_finished += 1

            # If finishing these columns wins me the game, let's do it
            if len(finished) + columns_finished >= 3:
                winning_move = move
                break
        return winning_move

    def compare_with_leader(self, leader_progress, my_progress, board, col):
        step_size = 1 / board[col]['steps']
        return (my_progress[col] - leader_progress[col]['progress']) / step_size

    def choose_move(self, moves, board, changes, invalid_move=False):
        leader_progress, my_progress = self.get_progress(board, changes)
        started = self.get_started_columns(changes)

        # Look for moves that let me win
        best_move = self.look_for_the_win(board, my_progress, moves)
        if best_move is not None:
            return best_move

        # Choose move based on best move value
        best_move = moves[0]
        best_move_value = self.determine_move_value(
            best_move, leader_progress, my_progress, board, started)

        for i in range(1, len(moves)):
            move = moves[i]
            move_value = self.determine_move_value(
                move, leader_progress, my_progress, board, started)
            if move_value > best_move_value:
                best_move = move
                best_move_value = move_value
        return best_move
