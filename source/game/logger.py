"""
Implement logger to use multiple levels of debug messages.
info: https://docs.python.org/2/howto/logging-cookbook.html#logging-cookbook

logger.error('This logs to screen and debug.log')

logger.debug('This logs to debug.log')
"""


import logging
import os

logger = logging.getLogger('Colonies_Logger')
logger.setLevel(logging.DEBUG)

# Create file handler which logs even debug messages.
os.remove('debug.log')
fh = logging.FileHandler('debug.log')
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)-15s: %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)
