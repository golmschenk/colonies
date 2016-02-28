"""
The models file for the interface app.
"""
import pickle

from django.db import models

from source.game.game import Game as CoreGame
from source.game.player import Player as CorePlayer
from source.game.board import Board as CoreBoard
from source.game.piece import Piece as CorePiece


class GameManager(models.Manager):
    """
    The Game object manager.
    """
    def create_game(self):
        """
        A create function for the Game model which initializes the game data.

        :return: The newly created game object.
        :rtype: Game
        """
        game_data = pickle.dumps(CoreGame.new_game(self.default_board()))
        game = self.create(data=game_data)
        return game

    def default_board(self):
        """
        Setups a default board to be used.

        :return: The string representation of the Board object.
        :rtype: string
        """
        only_board = '1 . . . .\n. . . . .\n. . . . .\n. . . . .\n. . . . 2\n'
        return only_board


class Game(models.Model):
    """
    The database model to hold game information and data.
    """
    objects = GameManager()
    data = models.BinaryField(default=None)

    @property
    def board(self):
        """
        Retrieves the board array from the pickled game data.

        :return: The list of board rows
        :rtype: list[str]
        """
        unpickled_data = pickle.loads(self.data)
        board_rows = unpickled_data.board.replace(' ', '').splitlines()
        board_array = [list(row) for row in board_rows]
        return board_array

    @staticmethod
    def player_color(player_symbol):
        """
        Gets the color for the players symbol.

        :param player_symbol: The character that represents the players piece.
        :type player_symbol: str
        :return: The string of the color for that player. None if not a player piece.
        :rtype: str or None
        """
        colors = ['red', 'blue', 'green', 'yellow', 'purple', 'teal', 'brown', 'magenta']
        try:
            return colors[int(player_symbol)-1]
        except ValueError:
            return None

    @property
    def display_board(self):
        """
        Gets the board in display form.

        :return: The display array for the board.
        :rtype: list[list[str or None]]
        """
        return [[self.player_color(cell) for cell in row] for row in self.board]

    @property
    def status(self):
        """
        Retrieves the status from the pickled game data.

        :return: The status string
        :rtype: str
        """
        unpickled_data = pickle.loads(self.data)
        return unpickled_data.status

    def move(self, current_x, current_y, new_x, new_y):
        """
        Executes the move of a piece.

        :param current_x: Current x position of piece to move.
        :type current_x: int
        :param current_y: Current y position of piece to move.
        :type current_y: int
        :param new_x: The x position to move the piece to.
        :type new_x: int
        :param new_y: The y position to move the piece to.
        :type new_y: int
        """
        core_game = pickle.loads(self.data)
        core_game.make_move((current_x, current_y), (new_x, new_y))
        self.data = pickle.dumps(core_game)
