

import serial

# Configure the serial port
ser = serial.Serial('/dev/cu.usbserial-110', baudrate=115200, timeout=1)  # Replace with the appropriate serial port

try:
    while True:
        # Read a line of data from the serial port
        try:
            line = ser.readline().decode('utf-8').strip()
        except UnicodeDecodeError:
            print("Error decoding data. Ignoring the line.")
            continue

        # Check if the line starts with '$GPGGA', which is a common NMEA sentence for location data
        if line.startswith('$GNGGA'): 
            # Split the NMEA sentence into individual fields
            fields = line.split(',')

            # Extract relevant data fields
            if len(fields) >= 15:  # Adjust the field count as needed
                time = fields[1]  # Time (UTC)
                latitude = fields[2]  # Latitude (ddmm.mmmmm)
                longitude = fields[4]  # Longitude (dddmm.mmmmm)
                altitude = fields[9]  # Altitude (meters above mean sea level)
                num_satellites = fields[7]  # Number of satellites used
                hdop = fields[8]  # HDOP (Horizontal Dilution of Precision)
                age_of_satellite = fields[13]  # Age of satellite information
                checksum = fields[14]  # Checksum (optional)

                # Convert latitude and longitude to decimal degrees
                latitude_deg = float(latitude[:2]) + float(latitude[2:]) / 60
                longitude_deg = float(longitude[:3]) + float(longitude[3:]) / 60

                print(f"Time: {time}\nLatitude: {latitude_deg}\nLongitude: {longitude_deg}\nAltitude: {altitude} meters")
                print(f"Number of Satellites: {num_satellites}\nHDOP: {hdop}")
                if checksum:
                    print(f"Checksum: {checksum}")
                print("-----------------------------------------")
except KeyboardInterrupt:
    # Handle Ctrl+C to gracefully exit the loop
    pass

# Close the serial port when done
ser.close()


'''
import serial

# Configure the serial port
ser = serial.Serial('/dev/cu.usbserial-110', baudrate=1152000, timeout=1)  # Replace with the appropriate serial port

try:
    while True:
        # Read a line of data from the serial port
        try:
            line = ser.readline().decode('utf-8').strip()
        except UnicodeDecodeError:
            print("Error decoding data. Ignoring the line.")
            continue

        # Check if the line starts with any of the supported NMEA sentences
        if line.startswith('$GNGGA') or line.startswith('$GNGLL') or line.startswith('$GPGSA'):
            # Split the NMEA sentence into individual fields
            fields = line.split(',')

            # Extract relevant data fields based on the sentence type
            if line.startswith('$GNGGA') and len(fields) >= 10:
                time = fields[1]  # Time (UTC)
                latitude = fields[2]  # Latitude (ddmm.mmmmm)
                longitude = fields[4]  # Longitude (dddmm.mmmmm)
                altitude = fields[9]  # Altitude (meters above mean sea level)

                # Convert latitude and longitude to decimal degrees
                latitude_deg = float(latitude[:2]) + float(latitude[2:]) / 60
                longitude_deg = float(longitude[:3]) + float(longitude[3:]) / 60

                print(f"Time: {time}, Latitude: {latitude_deg}, Longitude: {longitude_deg}, Altitude: {altitude} meters")

            elif line.startswith('$GNGLL') and len(fields) >= 5:
                latitude = fields[1]  # Latitude (ddmm.mmmm)
                longitude = fields[3]  # Longitude (dddmm.mmmm)

                # Convert latitude and longitude to decimal degrees
                latitude_deg = float(latitude[:2]) + float(latitude[2:]) / 60
                longitude_deg = float(longitude[:3]) + float(longitude[3:]) / 60

                print(f"Latitude: {latitude_deg}, Longitude: {longitude_deg}")

            elif line.startswith('$GPGSA') and len(fields) >= 17:
                # Extract relevant data fields from the GSA sentence if needed
                pdop = fields[15]  # Position Dilution of Precision (PDOP)
                hdop = fields[16]  # Horizontal Dilution of Precision (HDOP)
                
                print(f"PDOP: {pdop}, HDOP: {hdop}")

except KeyboardInterrupt:
    # Handle Ctrl+C to gracefully exit the loop
    pass

# Close the serial port when done
ser.close()

'''

