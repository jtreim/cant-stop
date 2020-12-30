# cant-stop
This is a framework for testing out the best Can't Stop AI player! All game logic can be found in the [game.py](https://github.com/jtreim/cant-stop/blob/main/game.py), [board.py](https://github.com/jtreim/cant-stop/blob/main/board.py), [errors.py](https://github.com/jtreim/cant-stop/blob/main/errors.py), and [player.py](https://github.com/jtreim/cant-stop/blob/main/player.py) files.

## I wanna make a player!
The base [Player](https://github.com/jtreim/cant-stop/blob/main/player.py) class has everything ready to add more game logic. Simply subclass the Player class and override the is_continuing_turn and choose_move functions. No guarantees that your Player will still run if you mess with the other game files. My suggestion is that you clone the repo, make your own branch, make your own player file (e.g. "CameronsWinningestPlayer.py"), and we'll figure out how to add that in. If you need help, an example subclass can be found in the [example_player.py](https://github.com/jtreim/cant-stop/blob/main/example_player.py).

### Overriding the is_continuing_turn function
You should see example inputs in the file, but as a reference the inputs are:

- board: Dictionary containing board information.
       Example: 
       ```
       {
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
        ```
- changes: Dictionary with all the changes since the turn began.
         Example: 
         ```
         {
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
         ```

The game expects back a boolean stating whether or not your player wants to keep rolling dice.

### Overriding the choose_move function
You should see example inputs in the files, but as a reference the inputs are:

- moves: List of integers containing available moves for the player.
       Example: ```[[5,8], [6], [7], [4], [9]]```
                (in the case that 1, 3, 4, & 5 are rolled, and the player has started columns 5 & 8).
       The game will automatically end a turn if the player has no available moves.

- board: Dictionary containing board information.
       Example: 
       ```
       {
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
        ```

- changes: Dictionary with all the changes since the turn began.
         Example: 
         ```
         {
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
       ```

- invalid_move: A boolean flag stating whether the last move submitted was determined to be an invalid move by the game.

The game expects back a selected move from the list of moves given.
