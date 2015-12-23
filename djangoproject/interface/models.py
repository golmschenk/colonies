"""
The models file for the interface app.
"""
import pickle

from django.db import models

import sys  # For core game mock
from unittest.mock import Mock  # For core game mock
sys.modules['CoreGame'] = Mock()  # For core game mock
import CoreGame


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
        game_data = pickle.dumps(CoreGame())
        game = self.create(data=game_data)
        return game


class Game(models.Model):
    """
    The database model to hold game information and data.
    """
    objects = GameManager()
    data = models.BinaryField(default=None)

    @property
    def board_rows(self):
        """
        Retrieves the board rows from the pickled game data.

        :return: The list of board rows
        :rtype: list[str]
        """
        unpickled_data = pickle.loads(self.data)
        return unpickled_data.board.splitlines()

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
        core_game.move(current_x=current_x, current_y=current_y, new_x=new_x, new_y=new_y)
        self.data = pickle.dumps(core_game)
