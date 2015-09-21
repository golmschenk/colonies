"""This file contains the implementation for managing human and cpu player data."""


class Player:

    """The class for player data."""
    number_of_players = 0

    def __init__(self, index):
        """
        Constructor for Player class.
        :param index: The numberic identity of the player.
        :type index: int
        """
        Player.number_of_players += 1
        self.id = index


class HumPlayer(Player):

    """ Class that represents a human player. """

    def __init__(self, index):
        """
        Constructor for a HumPlayer Player class.
        :param index: The numberic identity of the player.
        :type index: int
        """
        super().__init__(index)

    def make_move(self):
        """
        Method to retrieve input from the user in the form of a move.
        :return: Two vectors that represent the piece and new locations accordingly.
        :rtype: vector, vector
        """
        piece_in = input("Piece:")
        piece = [int(s) for s in piece_in.split() if s.isdigit()]
        move_in = input("Move:")
        move = [int(s) for s in move_in.split() if s.isdigit()]
        return piece, move


class ComPlayer(Player):

    """ Class that represents a ComPlayer player. """

    def __init__(self, index, ai_string):
        """
        Constructor for a ComPlayer Player class.
        :param index: The numberic identity of the player.
        :type index: int
        :param ai_string: The string representation of the AI module.
        :type ai_string: string
        """
        super().__init__(index)
        self.ai_string = ai_string

    def make_move(self):
        return [0, 0], [0, 0]
