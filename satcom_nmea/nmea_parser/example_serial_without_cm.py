""" Example code to demonstrate using NMEA Parser without a context manager
"""

from nmea import input_stream

stream = input_stream.GenericInputStream.open_stream('/dev/ttyACM0', 9600)

print(stream)
print(stream.get_line())
stream.ensure_closed()      # You must not forget to manually close the stream.
