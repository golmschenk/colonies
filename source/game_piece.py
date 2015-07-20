""" Contains GamePiece object and methods """


class GamePiece:
    """ A GamePiece defines a generic unit that is involved in the game. """

    def __init__(self, player, width, height, piece_type):
        """
        Constructor for GamePiece class.

        :param player: The player which controls this piece. 0 is no player.
        :type player: int
        :param width: The X coordinate of the piece.
        :type width: int
        :param height: The Y coordinate of the piece.
        :type height: int
        :param piece_type: What type of piece it is.
        :type piece_type: int
        """
        self.player = player
        self.width = width
        self.height = height
        self.type = piece_type
