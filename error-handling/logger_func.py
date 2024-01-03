# https://limszezhong.medium.com/python-logging-a-quick-guide-and-some-code-087f9bcf639a

"""
It's better to set up a logger using getLogger() instead of logger.basicConfig():

When you call logging.basicConfig(), 
it sets up the logging system for the entire application. 
If this is called without any prior configurations, 
it configures the "root logger," 
which is the main logger for the entire application. 
This means that any logging calls made by other parts of the program 
without explicitly creating loggers will use these configurations.
"""

import logging


def build_logger(
    loggername=__name__,
    console_level=logging.WARNING,
    log_level=logging.DEBUG,
    logpath=None,
):
    """
    Creates logger object for detailed logging of python scripts. Parameters:
    loggername (str): name of logger. Can really be any string. Not sure if there is custom or best practice
    console_level: severity level you want for messages printed to console at run time. Default is to print WARNING and above
    log_level: severity level of messages printed to log file (if using log file). Generally, you'll want lower severity level for log file.
    logpath: path of log file where you want messages to print to.

    Jan 2023 desired update - add formatter option (e.g., so that all messages have
    date + time prepended to any message; maybe the function name too)

    more information - https://docs.python.org/3/howto/logging.html
    """
    logger = logging.getLogger(loggername)

    # use StreamHandler to set which severity level is printed to console at run time
    shandler = logging.StreamHandler()
    logger.addHandler(shandler)
    logger.setLevel(logging.DEBUG)
    shandler.setLevel(console_level)

    # if desired, can write log messages to file, and in theory indicate different severity level
    # (e.g., maybe for console you only want to print warning and above, while
    # for log file you want to include INFO or even DEBUG-level messages)
    if logpath:
        fhandler = logging.FileHandler(logpath, mode="w")
        fhandler.setLevel(log_level)
        logger.addHandler(fhandler)

    return logger


# Example creation of logger object.
logger1 = build_logger(
    loggername="LOGGER1",
    logpath="output_log.log",
    console_level=logging.INFO,
    log_level=logging.WARNING,
)


# example function that uses logger object to log outputs
def log_tester(logger_obj, x):
    if x == 0:
        logger_obj.debug(f"{x} - Debug message")
    elif x == 1:
        logger_obj.info(f"{x} - Info message")
    elif x == 2:
        logger_obj.warning(f"{x} - Warning message")
    elif x == 3:
        logger_obj.error(f"{x} - Error message")
    elif x == 4:
        logger_obj.critical(f"{x} - Critical message")
    else:
        print(f"{x} is out of range")

    # time.sleep(1)
    return


for i in range(5):
    print(f"\n{i}")
    log_tester(logger1, i)
