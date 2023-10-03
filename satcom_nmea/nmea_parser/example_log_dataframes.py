""" Example code to demonstrate logging DataFrames to a database
"""

from nmea import input_stream, data_frame, database_wrapper

stream = input_stream.GenericInputStream.open_stream('/dev/ttyACM0', baud=9600)

db = database_wrapper.SQLiteConnection.from_path('./example.sqlite')

print(stream)

with stream:
    while True:
        try:
            new_frame = data_frame.DataFrame.get_next_frame(stream)
        except ValueError:
            continue

        print("Current GPS time:", new_frame.gps_time)
        print("Current Latitude:", new_frame.latitude)
        print("Current Longitude:", new_frame.longitude)
        print("Current Speed:", new_frame.velocity)
        print("Current heading:", new_frame.track)
        print("Number of Satellites above:", new_frame.nsats)
        print("Individual Observations:")
        for obs in new_frame.sv_observations:
            print('\tPRN:', obs.prn)
            print('\t\tSignal to Noise:', obs.snr)
            print('\t\tAzimuth:', obs.azimuth)
            print('\t\tElevation:', obs.elevation)

        db.insert_dataframe(new_frame)
