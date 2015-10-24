"""
File for code related to testing a simple game.
"""

import os
import pytest

from .command_line_tester import CommandLineTester


class TestSimpleGame:
    """
    A test suite to test simple game play.
    """
    def test_a_simple_game_between_two_players(self):
        """
        A test which checks that two players can play a (very) simple game.
        """
        # Kara and Iris wish to play a game of colonies.
        # They run the game on the test_level_1.
        test_level_path = os.path.join('functional_tests', 'resources', 'test_level_1')
        command_line_tester = CommandLineTester('python3 main.py %s' % test_level_path)

        # Kara and Iris see that the program wants a piece to be chosen.
        assert command_line_tester.expect('Piece:')

        # Kara picks a piece.
        command_line_tester.send('0 0')

        # She then sees that the program wants a place to move the piece to.
        assert command_line_tester.expect('Move:')

        # Kara moves the piece.
        command_line_tester.send('0 1')

        # They now see it's Iris's turn.
        assert command_line_tester.expect('Piece:')

        # Iris never explained the rules. To teach them through example, she goes for the fastest win she can.
        # She picks a piece and moves it.
        command_line_tester.send('4 4')
        assert command_line_tester.expect('Move:')
        command_line_tester.send('2 2')

        # Curious about the cloning ability, Kara continues unsuspectingly.
        assert command_line_tester.expect('Piece:')
        command_line_tester.send('0 0')
        assert command_line_tester.expect('Move:')
        command_line_tester.send('1 0')

        # Kara goes for the kill.
        assert command_line_tester.expect('Piece:')
        command_line_tester.send('2 2')
        assert command_line_tester.expect('Move:')
        command_line_tester.send('1 1')

        # The game is completed with that move.
        assert command_line_tester.has_terminated()