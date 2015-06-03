"""This file contains the implementation for managing player data."""

class Player:
    """The class for player data."""
    number_of_players = 0

    def __init__(self):
        """Player object initilizer."""
        Player.number_of_players += 1
        self.id = Player.number_of_players