"""
The models file for the interface app.
"""
import pickle

from django.db import models


class Game(models.Model):
    """
    The database model to hold game information and data.
    """
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
