""" Contains GamePiece object and methods """
from source.game.logger import logger
from source.game.element import Element


class Piece(Element):

    """ A Piece defines a generic unit that is involved in the game. """

    def __init__(self, player, width, height, piece_type):
        """
        Constructor for Piece class.

        :param player: The player which controls this piece. 0 is no player.
        :type player: int
        :param width: The X coordinate of the piece.
        :type width: int
        :param height: The Y coordinate of the piece.
        :type height: int
        :param piece_type: What type of piece it is.
        :type piece_type: int
        """
        Element.__init__(self, width, height)
        self.player = player
        self.type = piece_type
        self.capture_count = 0
        self.move_count = 0

    def capture(self, player):
        """
        Used for passed Player to gain control of Piece

        :param player: The player to gain control of this Piece.
        :type player: Player
        """
        logger.debug("Piece at (%u,%u) owned by player=%u captured by player=%u.",
                     self.x, self.y, self.player.id, player.id)
        self.player = player
        self.type = player.id
        self.capture_count = self.capture_count + 1

    def move(self, x, y):
        """
        Relocates the passed piece on the gameboard.

        :param x: The new X coordinate for the piece.
        :type x: int
        :param y: The new Y coordinate for the piece.
        :type y: int
        """
        self.x = x
        self.y = y
        self.move_count = self.move_count + 1

    def is_clone_distance(self, x, y):
        """
        Make a copy of a piece.
        Has a max distance of one spaces
        (including diagonals).

        :param x: The proposed x-coordinate for the action.
        :type x: int
        :param y: The proposed y-coordinate for the action.
        :type y: int
        """
        delta_x = abs(self.x - x)
        delta_y = abs(self.y - y)
        if delta_x > 1:
            return False
        if delta_y > 1:
            return False
        if (delta_x is 0 and delta_y is 0):
            return False
        return True

    def is_jump_distance(self, x, y):
        """
        Moves a unit without creating a new piece.
        Has a max distance of two spaces
        (including diagonals).

        :param x: The proposed x-coordinate for the action.
        :type x: int
        :param y: The proposed y-coordinate for the action.
        :type y: int
        """
        delta_x = abs(self.x - x)
        delta_y = abs(self.y - y)
        if self.is_clone_distance(x, y):
            return False
        if delta_x > 2:
            return False
        if delta_y > 2:
            return False
        if delta_x is 0 and delta_y is 0:
            return False
        return True

    def clone(self, x, y):
        """
        Make a copy of a piece.

        :param x: The proposed x-coordinate for the action.
        :type x: int
        :param y: The proposed y-coordinate for the action.
        :type y: int
        """
        return Piece(self.player, x, y, self.type)

    def jump(self, x, y):
        """
        Moves a unit without creating a new piece.

        :param x: The proposed x-coordinate for the action.
        :type x: int
        :param y: The proposed y-coordinate for the action.
        :type y: int
        """
        self.move(x, y)

    def is_adjacent_to(self, piece):
        """
        Determine if the provided piece adject to self.

        :param x: The proposed x-coordinate for the action.
        :type x: int
        :param y: The proposed y-coordinate for the action.
        :type y: int
        :return int:
        """
        delta_x = abs(self.x - piece.x)
        delta_y = abs(self.y - piece.y)
        if delta_x is 1 and delta_y is 1:
            return True
        if delta_x is 1 and delta_y is 0:
            return True
        if delta_x is 0 and delta_y is 1:
            return True
        return False
