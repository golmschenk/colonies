"""
The models file for the interface app.
"""
from django.db import models


class Game(models.Model):
    """
    The database model to hold game information and data.
    """
    data = models.BinaryField(default=None)
