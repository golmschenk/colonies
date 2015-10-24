"""
File containing code for command line interaction for tests.
"""

import time
import sys
from functools import partial
from subprocess import PIPE, Popen, TimeoutExpired
from threading import Thread
from queue import Queue, Empty

ON_POSIX = 'posix' in sys.builtin_module_names


class CommandLineTester:
    """
    A class to allow for easy command line interaction during a test.
    """
    def __init__(self, command):
        self.process = Popen(command.split(), stdout=PIPE, stdin=PIPE, bufsize=0, close_fds=ON_POSIX)
        self.queue = Queue()
        self.thread = Thread(target=self.enqueue_output, args=(self.process.stdout, self.queue))
        self.thread.daemon = True
        self.thread.start()

    def enqueue_output(self, stdout, output_queue):
        """
        The process to queue the stdout of the thread.

        :param stdout: The stdout to queue.
        :type stdout: subprocess.PIPE
        :param output_queue: The queue to send the messages to.
        :type output_queue: queue.Queue
        """
        for line in iter(partial(stdout.read, 1), b''):
            output_queue.put(line)
        stdout.close()

    def expect(self, string):
        """
        Checks if the string is in the messaging queue of the threaded process.

        :param string: The string to find.
        :type string: str
        :return: Whether or not the string was found within a time limit.
        :rtype: bool
        """
        queue_string = ''
        for _ in range(100):
            try:
                while True:
                    queue_string += self.queue.get_nowait().decode()
            except Empty:
                pass
            if string in queue_string:
                return True
            time.sleep(0.1)
        return False

    def send(self, string, end='\n'):
        """
        Sends a string to the command line.

        :param string: The string to send.
        :type string: str
        :param end: The end of the string, by default a new line (to be used for `input()` execution).
        :type end: str
        """
        final_string = string + end
        self.process.stdin.write(final_string.encode())

    def has_terminated(self):
        """
        Checks if the command line program terminated.

        :return: True if terminated, false otherwise.
        :rtype: bool
        """
        try:
            self.process.wait(timeout=3)
            return True
        except TimeoutExpired:
            return False
