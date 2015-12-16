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
