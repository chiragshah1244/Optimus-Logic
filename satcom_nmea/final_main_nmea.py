

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
                print("----------------GNGGA-------------------------")

                print(f"Time: {time}\nLatitude: {latitude_deg}\nLongitude: {longitude_deg}\nAltitude: {altitude} meters")
                print(f"Number of Satellites: {num_satellites}\nHDOP: {hdop}")
                if checksum:
                    print(f"Checksum: {checksum}")
                
        
        if line.startswith('$GNGLL'):
       
            # Split the NMEA sentence into individual fields
            fields = line.split(',')
            
            if len(fields) >= 5:
                latitude = fields[1]  # Latitude (ddmm.mmmm)
                longitude = fields[3]  # Longitude (dddmm.mmmm)

                # Convert latitude and longitude to decimal degrees
                latitude_deg = float(latitude[:2]) + float(latitude[2:]) / 60
                longitude_deg = float(longitude[:3]) + float(longitude[3:]) / 60
                print("-------------------GNGGL----------------------")

                print(f"Latitude: {latitude_deg}\nLongitude: {longitude_deg}")
           

        if line.startswith('$GPGSA'):
       
            # Split the NMEA sentence into individual fields
            fields = line.split(',')
            
            if len(fields) >= 17:
                mode_fix_type = fields[2]  # Mode fix type (A: Auto, M: Manual)
                satellite_prns = fields[3:15]  # PRNs of active satellites
                pdop = fields[15]  # PDOP (Position Dilution of Precision)
                hdop = fields[16]  # HDOP (Horizontal Dilution of Precision)
                vdop = fields[17]  # VDOP (Vertical Dilution of Precision)
                print("------------------GPGSA-----------------------")

                print(f"Mode Fix Type: {mode_fix_type}")
                print(f"Satellite PRNs: {', '.join(satellite_prns)}")
                print(f"PDOP: {pdop}")
                print(f"HDOP: {hdop}")
                print(f"VDOP: {vdop}")

                
        
        if line.startswith('$GAGSA'):
       
            # Split the NMEA sentence into individual fields
            fields = line.split(',')
            
            if len(fields) >= 17:
                mode_fix_type = fields[2]  # Mode fix type (A: Auto, M: Manual)
                satellite_prns = fields[3:15]  # PRNs of active satellites
                pdop = fields[15]  # PDOP (Position Dilution of Precision)
                hdop = fields[16]  # HDOP (Horizontal Dilution of Precision)
                vdop = fields[17]  # VDOP (Vertical Dilution of Precision)
                print("---------------------GAGSA--------------------")

                print(f"Mode Fix Type: {mode_fix_type}")
                print(f"Satellite PRNs: {', '.join(satellite_prns)}")
                print(f"PDOP: {pdop}")
                print(f"HDOP: {hdop}")
                print(f"VDOP: {vdop}")    
               
                
        if line.startswith('$GIGSA'):
       
            # Split the NMEA sentence into individual fields
            fields = line.split(',')
            
            if len(fields) >= 17:
                mode_fix_type = fields[2]  # Mode fix type (A: Auto, M: Manual)
                satellite_prns = fields[3:15]  # PRNs of active satellites
                pdop = fields[15]  # PDOP (Position Dilution of Precision)
                hdop = fields[16]  # HDOP (Horizontal Dilution of Precision)
                vdop = fields[17]  # VDOP (Vertical Dilution of Precision)
                print("-------------------GIGSA----------------------")

                print(f"Mode Fix Type: {mode_fix_type}")
                print(f"Satellite PRNs: {', '.join(satellite_prns)}")
                print(f"PDOP: {pdop}")
                print(f"HDOP: {hdop}")
                print(f"VDOP: {vdop}")    
                
             
        if line.startswith('$BDGSA'):
       
            # Split the NMEA sentence into individual fields
            fields = line.split(',')
            
            if len(fields) >= 17:
                mode_fix_type = fields[2]  # Mode fix type (A: Auto, M: Manual)
                satellite_prns = fields[3:15]  # PRNs of active satellites
                pdop = fields[15]  # PDOP (Position Dilution of Precision)
                hdop = fields[16]  # HDOP (Horizontal Dilution of Precision)
                vdop = fields[17]  # VDOP (Vertical Dilution of Precision)
                print("---------------------BDGSA--------------------")

                print(f"Mode Fix Type: {mode_fix_type}")
                print(f"Satellite PRNs: {', '.join(satellite_prns)}")
                print(f"PDOP: {pdop}")
                print(f"HDOP: {hdop}")
                print(f"VDOP: {vdop}")    
               
        '''        
        if line.startswith('$GIGSV'):    
            
            fields = line.split(',')
            
            if len(fields) >= 7:  # Adjust the field count as needed
                num_sentences = int(fields[1])  # Number of sentences for this data
                sentence_num = int(fields[2])  # Sentence number (1-based)
                num_satellites = int(fields[3])  # Number of satellites in view

                # Initialize a list to store satellite information
                satellites = []

                # Extract satellite data
                for i in range(4, len(fields), 4):
                    if i + 3 < len(fields):
                        prn = int(fields[i])  # Satellite PRN number
                        elevation = int(fields[i + 1])  # Elevation in degrees
                        azimuth = int(fields[i + 2])  # Azimuth in degrees
                        snr = int(fields[i + 3])  # Signal-to-Noise Ratio (SNR) in dB

                        satellites.append({"PRN": prn, "Elevation": elevation, "Azimuth": azimuth, "SNR": snr})

                print(f"Number of Sentences: {num_sentences}")
                print(f"Sentence Number: {sentence_num}")
                print(f"Number of Satellites in View: {num_satellites}")

                for satellite in satellites:
                    print(f"Satellite PRN: {satellite['PRN']}, Elevation: {satellite['Elevation']} degrees")
                    print(f"Azimuth: {satellite['Azimuth']} degrees, SNR: {satellite['SNR']} dB")    
                       ''' 
                
        
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

