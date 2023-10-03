""" Contains code to set up output via Python's built in logging facility
"""

import logging

_LOGGING_CONFIGURED = False
LOGGER_NAME = 'nmea-parser'


def _set_up_logging():
    """ Set up the NMEA Parser logger. Only allowed to execute once.
    """

    global _LOGGING_CONFIGURED

    if _LOGGING_CONFIGURED:
        logging.getLogger(LOGGER_NAME).warning('`set_up_logging()` called more than once.')
        return

    _LOGGING_CONFIGURED = True

    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(levelname)-8s [%(filename)s]: %(message)s")
    handler.setFormatter(formatter)
    handler.setLevel(logging.WARNING)

    logging.getLogger(LOGGER_NAME).addHandler(handler)


def get_logger() -> logging.Logger:
    """ Get the NMEA Parser Logger

    :return: The NMEA Parser logger

    """

    return logging.getLogger(LOGGER_NAME)


if not _LOGGING_CONFIGURED:
    _set_up_logging()
