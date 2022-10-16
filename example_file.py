from tournament import Tournament
from players.CameronPlayer import CameronPlayer

tournament = Tournament()
tournament.add_player('Cameron', CameronPlayer)
tournament.add_player('Cameron2', CameronPlayer)
tournament.run()