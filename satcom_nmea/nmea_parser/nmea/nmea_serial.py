""" Example code to demonstrate using NMEA Parser with a context manager
"""

from nmea import input_stream

stream = input_stream.GenericInputStream.open_stream('/dev/cu.usbserial-110')

print(stream)

with stream:
    print(stream.get_line())