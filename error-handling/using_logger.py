

"""
using_logger.py
Some examples for how to log stuff using the standard logger library. Use cases:
* Debugging what happened
* Generally more advanced way to log instead of writing a bunch of print statements.

# https://medium.com/analytics-vidhya/how-to-run-machine-learning-experiments-with-python-logging-module-9030fbee120e
# https://docs.python.org/3/howto/logging.html
# https://docs.python.org/3/howto/logging.html#changing-the-format-of-displayed-messages # left off here on 7/10/22
# https://realpython.com/python-logging/

Logging levels (listed in order from least to most serious; default is warning):

    DEBUG = Detailed information, typically of interest only when diagnosing problems.

    INFO = Confirmation that things are working as expected.

    WARNING = An indication that something unexpected happened, 
        or indicative of some problem in the near future (e.g. ‘disk space low’). 
        The software is still working as expected.

    ERROR = Due to a more serious problem, the software has not been able to perform some function.

    CRITICAL = A serious error, indicating that the program itself may be unable to continue running.

"""

import logging


# configuring how you log 

example_logfile = 'example_logfile.log'

# what and how you want to format the logged message.
# lots of potential attributes you can log, e.g. timestamtp, error level number, etc.
#full list of attributes you can log: https://docs.python.org/3/library/logging.html#logrecord-attributes
output_format = "%(levelname)s: %(msg)s %(asctime)s"

logging.basicConfig(
    filename=None, # output log file. If None will print to console
    filemode='w', # either 'a' (append) or 'w' (overwrite) the log content to the file. 
    level=logging.DEBUG, # what level/severity of messages you want logged. See above for details.
    format=output_format, # how you want to format output.
    ) 

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

