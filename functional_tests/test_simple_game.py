"""
File for code related to testing a simple game.
"""

import os
import pytest

from main import main


class TestSimpleGame:
    """
    A test suite to test simple game play.
    """
    def test_a_simple_game_between_two_players(self):
        """
        A test which checks that two players can play a (very) simple game.
        """
        # Kara and Iris wish to play a game of colonies.
        # They run the game on the test_level.
        # (We'll cheat a bit here in that we'll call main() directly opposed to calling it from the command
        # line as Kara and Iris would)
        test_level_path = os.join('functional_tests', 'resources', 'test_level')
        main(['', test_level_path])  # Index 0 is the name of the script, but can be blank in the test.
