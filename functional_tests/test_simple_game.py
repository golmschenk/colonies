"""
File for code related to testing a simple game.
"""

import os
import pytest
import time
import sys
from functools import partial
from subprocess import PIPE, Popen
from threading import Thread
from queue import Queue, Empty

ON_POSIX = 'posix' in sys.builtin_module_names


class TestSimpleGame:
    """
    A test suite to test simple game play.
    """
    def output_queue_contains_string(self, string_to_find, queue):
        queue_string = ''
        for _ in range(100):
            try:
                while True:
                    queue_string += queue.get_nowait().decode()
            except Empty:
                pass
            if string_to_find in queue_string:
                return True
            time.sleep(0.1)
        return False

    def test_a_simple_game_between_two_players(self):
        """
        A test which checks that two players can play a (very) simple game.
        """
        # Kara and Iris wish to play a game of colonies.
        # They run the game on the test_level.
        # (Huge ridiculous setup to get input and output testing on the command line working properly)
        def enqueue_output(stdout, output_queue):
            for line in iter(partial(stdout.read, 1), b''):
                output_queue.put(line)
            stdout.close()

        test_level_path = os.path.join('functional_tests', 'resources', 'test_level')
        process = Popen(['python3', 'main.py', test_level_path], stdout=PIPE, stdin=PIPE, bufsize=0, close_fds=ON_POSIX)
        queue = Queue()
        thread = Thread(target=enqueue_output, args=(process.stdout, queue))
        thread.daemon = True
        thread.start()

        # Kara and Iris see that the program wants a piece to be chosen.
        assert self.output_queue_contains_string('Piece:', queue)

        # Kara picks a piece.
        process.stdin.write('0 0\n'.encode())

        # She then sees that the program wants a place to move the piece to.
        assert self.output_queue_contains_string('Move:', queue)

        # Kara moves the piece.
        process.stdin.write('0 1\n'.encode())

        # They now see it's Iris's turn.
        assert self.output_queue_contains_string('Move:', queue)
