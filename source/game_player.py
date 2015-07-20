"""This file contains the implementation for managing player data."""


class GamePlayer:
    """The class for player data."""
    number_of_players = 0

    def __init__(self):
        """Player object initilizer."""
        GamePlayer.number_of_players += 1
        self.id = GamePlayer.number_of_players
