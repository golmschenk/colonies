"""
The models file for the interface app.
"""
from django.db import models


class Game(models.Model):
    data = models.BinaryField(default=None)
