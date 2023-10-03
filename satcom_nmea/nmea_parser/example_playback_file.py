""" Example to show how to control library logging
"""

from nmea import input_stream, data_frame

stream = input_stream.GenericInputStream.open_stream('sample-data/sample1.txt')

with stream:
    new_frame = data_frame.DataFrame.get_next_frame(stream)

    print("Current GPS time:", new_frame.gps_time)
    print("Current Latitude:", new_frame.latitude)
    print("Current Longitude:", new_frame.longitude)
    print("Current Speed:", new_frame.velocity)
    print("Current heading:", new_frame.track)

