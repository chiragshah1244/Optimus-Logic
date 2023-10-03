""" A module to interpolate current time from GPS.

This will not be as accurate as system time, so do not use this. This module only exists to help track SV observations,
since we cannot expect every computer this code runs on to have an accurate system clock.
"""

from typing import Union
import time as py_time
import datetime

_CURRENT_GPST = None
_GPST_LAST_MONO = None


def time() -> Union[None, float]:
    """ Get current epoch time

    :return: Epoch time derived from GPS time

    """

    if _CURRENT_GPST is None:
        return None

    assert isinstance(_GPST_LAST_MONO, float)
    assert isinstance(_CURRENT_GPST, float)

    since_update = py_time.monotonic() - _GPST_LAST_MONO
    return _CURRENT_GPST + since_update


def gps_timestamp() -> Union[None, str]:
    """ Get current time in YYYY-MM-DD HH:MM:SS format

    :return: Current timestamp as string
    rea
    """

    now = time()
    if now is None:
        return None

    return datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


def report_gpst(gpst: str):
    """ Update GPS time

    :param gpst:
    :return:
    """

    now = py_time.monotonic()

    global _CURRENT_GPST
    global _GPST_LAST_MONO

    _CURRENT_GPST = py_time.mktime(py_time.strptime(gpst, '%Y-%m-%d %H:%M:%S'))
    _GPST_LAST_MONO = now
