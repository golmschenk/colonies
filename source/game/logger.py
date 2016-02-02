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
if os.path.exists('debug.log'):
    try:
        os.remove('debug.log')
    # Since the logger is on the root level of the script, it is run whenever the file is imported.
    # When running the Django server, this is called multiple times and on Windows
    # this results in a bug trying to remove the file when it's in use. This works around that.
    except:
        pass
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
