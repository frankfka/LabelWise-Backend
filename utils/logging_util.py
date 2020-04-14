import logging
import sys

__FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")


def __get_console_handler__():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(__FORMATTER)
    return console_handler


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)  # better to have too much log than not enough
    logger.addHandler(__get_console_handler__())
    logger.propagate = False
    return logger
