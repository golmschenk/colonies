"""This file manages unit data. By unit, we're talking about a game piece which a player owns."""

class Unit:
    """The class for unit data."""
    def __init__(self, owner):
        """
        Object initializer.
        :param owner: This should be the player object that owns the piece
        """
        self.owner = owner
